import fileinput
import sys
from collections import deque

from parsers.rst import RstParser


class Formatter:
    def __init__(self, file_path, dry_run):
        self.file = file_path
        self.dry_run = not dry_run
        self.parser = RstParser()

    def format(self, function):
        formatted_texts = self.format_texts(function)
        return self._restruct(function, formatted_texts)

    def _restruct(self, function, strings) -> None:
        with fileinput.input(files=self.file, inplace=self.dry_run) as f:
            lines = function.docstring.count('\n') + 1
            finished = False
            for line in f:
                n = f.filelineno()
                start_line = function.line_number
                if n <= start_line:
                    sys.stdout.write('%s' % line)
                    continue
                if start_line <= n and n <= start_line + lines:
                    while strings:
                        string = strings.popleft()
                        if string is '':
                            sys.stdout.write('\n')
                        else:
                            sys.stdout.write(
                                '%s%s\n' % (' ' * (function.offset + 4), string)
                            )
                else:
                    if finished:
                        sys.stdout.write('%s' % line)
                    else:
                        if '"""' in line or "'''" in line:
                            finished = True

    def format_texts(self, func) -> deque:
        def get_formatted_text(field):
            text = []
            for body in field:
                if body.tagname is 'field_name':
                    text.append(':%s:' % body.rawsource)
                else:
                    text.append('%s' % body.rawsource.replace('\n', ' '))
            return ' '.join(text)

        document = self.parser.parse(func.docstring, "")
        b = deque()
        b.append("'''")
        first = True
        for t in document.children:
            for x in t:
                if hasattr(x, 'children') and not isinstance(x, str):
                    for y in x:
                        if y.tagname == 'field_name':
                            if first:
                                b.append('')
                                first = False
                            text = get_formatted_text(y.parent.children)
                            b.append(text)
                else:
                    x = str(x)
                    t2 = x.split(' ')
                    t4 = []
                    for a in t2:
                        if a is not '':
                            t4.append(
                                a.replace('\n', '\n%s' % (' ' * (func.offset + 4)))
                            )
                    b.append(' '.join(t4))
        b.append("'''")
        return b
