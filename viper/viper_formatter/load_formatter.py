from . import rst_formatter


def load(file_path, style='RST', *, dry_run=False):
    if style == 'RST':
        return rst_formatter.Formatter(file_path, dry_run)
