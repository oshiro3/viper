import fileinput
import sys
from collections import deque

from parsers.rst import RstParser


def format_oneline(strings, line):
    if strings:
        while strings:
            sys.stdout.write('%s' % strings.popleft())
        else:
            sys.stdout.write('\n')
    if '"""' not in line:
        sys.stdout.write('%s' % line)


class Formatter:
    def __init__(self, file_path: str, dry_run: bool):
        self.file = file_path
        self.dry_run = not dry_run
        self.parser = RstParser()

    def format(self, index, function):
        formatted_texts = self._format_texts(function)
        return self._restruct(function, formatted_texts, index)

    def _restruct(self, function, strings: deque, func_count: int) -> None:
        with fileinput.input(files=self.file, inplace=self.dry_run) as f:
            lines = function.docstring.count('\n') + 1
            finished = False
            first = True
            start_line = function.line_number
            count = 1
            diff = 0
            for line in f:
                if 'def' in line:
                    if count == func_count:
                        # print('%d: %d' % (start_line, f.filelineno()))
                        diff = f.filelineno() - start_line
                    count += 1
                n = f.filelineno()
                if n <= start_line + diff:
                    sys.stdout.write('%s' % line)
                    continue
                if lines == 1:
                    if first:
                        sys.stdout.write('%s' % (' ' * (function.offset + 4)))
                        first = False
                    format_oneline(strings, line)
                    continue
                if start_line + diff <= n and n <= (start_line + lines + diff):
                    while strings:
                        string = strings.popleft()
                        if string == '':
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

    def _format_texts(self, func) -> deque:
        def get_formatted_text(field):
            text = []
            for body in field:
                if body.tagname == 'field_name':
                    text.append(':%s:' % body.rawsource)
                else:
                    text.append('%s' % body.rawsource.replace('\n', ' '))
            return ' '.join(text)

        document = self.parser.parse(func.docstring, "")
        b = deque()
        b.append('"""')
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
                        if a != '':
                            t4.append(
                                a.replace('\n', '\n%s' % (' ' * (func.offset + 4)))
                            )
                    b.append(' '.join(t4))
        b.append('"""')
        return b
