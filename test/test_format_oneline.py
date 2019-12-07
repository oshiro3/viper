from os import path
import sys
import shutil

sys.path.append(path.join(path.dirname(__file__), '../viper'))

from viper import reader
from viper.viper_formatter import load_formatter

expected = '''def function(arg1, arg2, arg3):
    """Hello, func"""
    pass\n'''


class TestGroup(object):
    def test_should_format_started_by_no_newline(self):
        file_path = path.join(
            path.dirname(path.abspath(__file__)), path.join('data', 'oneline.py')
        )
        test_path = path.join(
            path.dirname(path.abspath(__file__)), path.join('data', 'tmp', 'test.py')
        )
        shutil.copy(file_path, test_path)
        funcs = reader.extract_funcs(test_path)

        formatter = load_formatter.load(test_path)

        for func in funcs:
            formatter.format(func)
        with open(test_path) as f:
            s = f.read()
            assert s == expected
