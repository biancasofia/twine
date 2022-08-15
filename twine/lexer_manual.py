from lark import Token
from typing import Iterable
import re

REGEX_MAP = [
    ("BOOLEAN", r"true|false"),
    ("COMMA", r","),
    ("COMMENT", r"%.*"),
    ("EQUAL", r"="),
    ("F", r"F"),
    ("HAT", r"^"),
    ("INTEGER", r"0|[1-9][0-9]*"),
    ("IDENTIFIER", r"[a-zA-Z0-9$][a-zA-Z0-9_$]*"),
    ("LPAR", r"\("),
    ("LESS", r"<"),
    ("MINUS", r"-"),
    ("MUL", r"\*"),
    ("PIPE", r"|"),
    ("PLUS", r"\+"),
    ("RETURNS", r"returns"),
    ("RPAR", r"\\)"),
    ("SEMICOLON", r";"),
    ("DIV", r"\/"),
    ("TILDE", r"\~"),
]

def classifica(caracs: str) -> str:
    for (name, regex) in REGEX_MAP:
        if re.fullmatch(regex, caracs):
            return name
    raise SyntaxError(f'elemento nao reconhecido: {caracs}')

def lex(src: str) -> Iterable[Token]:
    caracteres = src.split()
    for caracs in caracteres:
        tipo = classifica(caracs)
        if tipo != "COMMENT":
            yield Token(tipo, caracs)

