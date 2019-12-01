import ast

from function import parse


def open_file(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as fin:
        return fin.read()


def extract_funcs(filename):
    program = open_file(filename)
    tree = ast.parse(program)
    return parse.create_function_details(tree)

