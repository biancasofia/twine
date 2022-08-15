from typing import Iterable
from lark import Token

from .gramatica import GRAMMAR

def lex(src: str) -> Iterable[Token]:
    return GRAMMAR.lex(src)