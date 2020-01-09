from logging import getLogger, config, Logger
from os import path
from typing import Union
# import argparse

from engine import engine


def create_logger() -> Union[Logger]:
    log_config_path = path.join(path.dirname(path.abspath(__file__)), 'logger.conf')
    config.fileConfig(log_config_path)
    return getLogger(__name__)


if __name__ == '__main__':
    # logger = create_logger()
    # parser = argparse.ArgumentParser(description='Process args')
    # parser.add_argument(
    #     'filename',
    #     metavar='filename',
    #     # nargs='+',
    #     help='filename for the formatter',
    # )
    # args = parser.parse_args()
    file_path = path.join(path.dirname(path.abspath(__file__)), "../sample.py")
    # if path.isfile(file_path):
    #
    engine = engine.load_engine('rst')
    engine.run(file_path)
    # funcs = reader.extract_funcs(file_path)
    #
    # formatter = load_formatter.load(file_path, dry_run=False)
    #
    # for i, func in enumerate(funcs, 1):
    #     formatter.format(i, func)
