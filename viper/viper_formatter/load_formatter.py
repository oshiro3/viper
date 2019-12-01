
from . import rst_formatter


def load(file_path, style='RST'):
    if style == 'RST':
        return rst_formatter.Formatter(file_path)
