from os import path
import sys
import shutil
import tempfile

sys.path.append(path.join(path.dirname(__file__), '../viper'))

from viper import reader
from viper.viper_formatter import load_formatter

expected = """def function(arg1, arg2, arg3):
    '''
    Hello, func
    korem ipsum dolor sit amet,

    :param string arg1: First argument
    :param arg2: Second argument
    :type args2: list[int]
    :param arg3: Third argument
    :type args3: dict[str, int]
    :return: Return value
    :rtype: str or None
    :raises ValueError: if arg1 is empty string. only string.
    '''
    pass\n"""


class TestGroup(object):
    def test_should_format_started_by_no_newline(self):
        file_path = path.join(
            path.dirname(path.abspath(__file__)), "data\\no_newline.py"
        )
        test_path = tempfile.TemporaryFile().name
        shutil.copy(file_path, test_path)
        funcs = reader.extract_funcs(test_path)

        formatter = load_formatter.load(test_path)

        for func in funcs:
            formatter.format(func)
        with open(test_path) as f:
            s = f.read()
            assert s == expected

    def test_should_format_has_remove_newline(self):

        file_path = path.join(
            path.dirname(path.abspath(__file__)), "data\\has_newline_in_sentence.py"
        )
        test_path = tempfile.TemporaryFile().name
        shutil.copy(file_path, test_path)
        funcs = reader.extract_funcs(test_path)

        formatter = load_formatter.load(test_path)

        for func in funcs:
            formatter.format(func)
        with open(test_path) as f:
            s = f.read()
            assert s == expected
