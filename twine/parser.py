from lark import Lark, Tree, Token
from pathlib import Path
from .gramatica import GRAMMAR
from typing import  Iterable


GRAMMAR_PATH = Path(__file__).parent / "twine.lark"
GRAMMAR_SRC = GRAMMAR_PATH.read_text()


def parse(src: str) -> Tree:
    return GRAMMAR.parse(src)



   