from logging import getLogger, config, Logger
from os import path
from typing import Union
import glob
# import argparse

import reader
from viper_formatter import load_formatter


def create_logger() -> Union[Logger]:
    log_config_path = path.join(path.dirname(path.abspath(__file__)), 'logger.conf')
    config.fileConfig(log_config_path)
    return getLogger(__name__)


def listup_files(dirs: Union[str]):
    for p in glob.glob(dirs, recursive=True):
        yield path.abspath(p)


def main(arg):
    # logger = create_logger()
    # parsers = argparse.ArgumentParser(description='Process args')
    # parsers.add_argument(
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

        funcs = reader.extract_funcs(file)

        formatter = load_formatter.load(file, dry_run=False)

        for i, func in enumerate(funcs, 1):
            formatter.format(i, func)


if __name__ == '__main__':
    main("../sample_2.py")
