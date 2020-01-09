from . import rst_engine


def load_engine(kind):
    if kind == 'rst':
        return rst_engine.RstEngine()
