from .reader import reader
from .viper_formatter import rst_formatter


class RstEngine(object):
    def run(self, file_path):
        funcs = reader.extract_funcs(file_path)

        formatter = rst_formatter.Formatter(file_path, dry_run=False)

        for i, func in enumerate(funcs, 1):
            formatter.format(i, func)
