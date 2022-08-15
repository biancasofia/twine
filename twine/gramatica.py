from lark import Lark
from pathlib import Path

TWINE_PATH = Path(__file__).parent
GRAMMAR_PATH = TWINE_PATH / "twine.lark"
GRAMMAR_SRC = GRAMMAR_PATH.read_text()
GRAMMAR = Lark(GRAMMAR_SRC, start="program")