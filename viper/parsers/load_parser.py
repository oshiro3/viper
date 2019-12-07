from . import rst


def load_parser(style='RST'):
    if style == 'RST':
        return rst.RstParser()
