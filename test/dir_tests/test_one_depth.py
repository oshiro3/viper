from os import path
import sys
import shutil
import glob

sys.path.append(path.join(path.dirname(__file__), '../../viper'))

from viper import viper

expected = '''def function(arg1, arg2, arg3):
    """
    Hello, func
    korem ipsum dolor sit amet,

    :param string arg1: First argument
    :param arg2: Second argument
    :type args2: list[int]
    :param arg3: Third argument
    :type args3: dict[str, int]
    :return: Return value
    :rtype: str or None
    :raises ValueError: if arg1 is empty string.
    """
    pass\n'''

exe_dir = path.join(path.dirname(path.abspath(__file__)), '../')


class TestGroup(object):
    def test_should_format_started_by_no_newline(self):
        dir_path = path.join(
            exe_dir, path.join('data', 'one_depth')
        )
        test_path = path.join(
            exe_dir, path.join('data', 'tmp', 'test.py')
        )
        test_path2 = path.join(
            exe_dir, path.join('data', 'tmp', 'test2.py')
        )
        dir_path += '/*.py'
        test_paths = [path.abspath(p) for p in glob.glob(dir_path)]
        shutil.copy(test_paths[0], test_path)
        shutil.copy(test_paths[1], test_path2)

        viper.main(path.dirname(test_path))

        with open(test_path) as f:
            s = f.read()
            print(s)
            assert s == expected

        with open(test_path2) as f:
            s = f.read()
            assert s == expected
