import ast
from typing import Iterator, List, Union

FunctionDef = ast.FunctionDef


def _find_docstring(func: ast.AST) -> str:
    return ast.get_docstring(func)


def _find_all_functions(
    tree: ast.AST,
) -> Iterator[Union[ast.FunctionDef, ast.AsyncFunctionDef]]:
    for node in ast.walk(tree):
        if isinstance(node, FunctionDef):
            yield node


def _find_all_classes(tree: ast.AST) -> Iterator[ast.ClassDef]:
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            yield node


def _find_all_methods(
    tree: ast.AST,
) -> Iterator[Union[ast.FunctionDef, ast.AsyncFunctionDef]]:
    for cls in _find_all_classes(tree):
        for fun in _find_all_functions(cls):
            yield fun


def find_docstring(fun: ast.AST) -> str:
    return ast.get_docstring(fun)


def get_line_number_from_function(fnc) -> int:
    line_number = fnc.lineno
    if hasattr(fnc, "args") and fnc.args.args:
        last_arg = fnc.args.args[-1]
        line_number = last_arg.lineno
    return line_number


def open_file(filename: str) -> str:
    with open(filename, "r") as fin:
        return fin.read()


class FunctionDetail(object):
    def __init__(
        self, is_method: bool, function: Union[ast.FunctionDef, ast.AsyncFunctionDef]
    ) -> None:
        self.is_method = is_method
        self.function = function
        self.name = function.name
        self.line_number = get_line_number_from_function(function)
        self.docstring = find_docstring(function)
        self.offset = function.col_offset


def create_function_details(src: ast.AST) -> List[FunctionDetail]:
    fds = list()  # type: List[FunctionDetail]

    methods = set(_find_all_methods(src))
    for method in methods:
        fds.append(FunctionDetail(is_method=True, function=method))

    functions = set(_find_all_functions(src)) - methods
    for function in functions:
        fds.append(FunctionDetail(is_method=False, function=function))

    return fds


if __name__ == "__main__":

    filename = "../sample.py"
    program = open_file(filename)
    tree = ast.parse(program)
    # print(tree)
    y = create_function_details(tree)
    for i in y:
        logger.debug(i.line_number)
        logger.debug(i.docstring)
        # print(i.docstring)
    # print(y)
    # print(docstring)
