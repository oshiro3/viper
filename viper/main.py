from logging import getLogger, config, Logger
from os import path
from typing import Union
import glob
# import argparse

from engine import engine


def create_logger() -> Union[Logger]:
    log_config_path = path.join(path.dirname(path.abspath(__file__)), 'logger.conf')
    config.fileConfig(log_config_path)
    return getLogger(__name__)


def listup_files(dirs: Union[str]):
    for p in glob.glob(dirs, recursive=True):
        yield path.abspath(p)


def main(arg):
    # logger = create_logger()
    # parser = argparse.ArgumentParser(description='Process args')
    # parser.add_argument(
    #     'filename',
    #     metavar='filename',
    #     # nargs='+',
    #     help='filename for the formatter',
    # )
    # args = parsers.parse_args()

    targets = path.join(path.dirname(path.abspath(__file__)), arg)
    if path.isdir(targets):
        targets += "/*.py"

    for file in listup_files(targets):
        # print(file)

        fomat_engine = engine.load_engine('rst')
        fomat_engine.run(file)


if __name__ == '__main__':
    main("../sample_2.py")
