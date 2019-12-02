from logging import getLogger, config, Logger
from os import path
from typing import Union
import argparse

import reader
from viper_formatter import load_formatter


def create_logger() -> Union[Logger]:
    log_config_path = path.join(path.dirname(path.abspath(__file__)), 'logger.conf')
    config.fileConfig(log_config_path)
    return getLogger(__name__)


if __name__ == '__main__':
    # logger = create_logger()
    # parsers = argparse.ArgumentParser(description='Process args')
    # parsers.add_argument(
    #     'filename',
    #     metavar='filename',
    #     # nargs='+',
    #     help='filename for the formatter',
    # )
    # args = parsers.parse_args()
    file_path = path.join(path.dirname(path.abspath(__file__)), "../sample_2.py")
    # if path.isfile(file_path):
    #
    funcs = reader.extract_funcs(file_path)

    formatter = load_formatter.load(file_path, dry_run=True)

    for func in funcs:
        formatter.format(func)
