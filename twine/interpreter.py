from collections import ChainMap
from typing import Union, Tuple, Dict, List, Iterator, Callable, MutableMapping, cast

from .ir import IR, SExpr, Declaration, ArgDefs
from .stdlib import GLOBALS

Value = Union[bool, int, Callable]

Env = MutableMapping[str, Value]


def eval(sexpr: SExpr, env: Env) -> Value:
    if type(sexpr) == list:
        
        carac = sexpr[0]
        
        b = sexpr[2]

        a = eval(sexpr[1], env)
        #se if
        if carac == "if":
            if (len(sexpr) == 4):

                if(sexpr[1] == True):

                        return eval(default_env()["if1"](a,b,sexpr[3]), env)
                else:

                    return eval(default_env()["if2"](a,sexpr[2],sexpr[3]), env)
        #ou
        elif carac == "|":
            if(sexpr[1] == True):

                return default_env()["|"](a,b)

            else:

                return eval(default_env()["|2"](a,eval(b, env)), env)

        elif carac == "^":

            if(sexpr[1] == False):

                return default_env()["|"](a,b)

            else:

                return eval(default_env()["|2"](a,eval(b, env)), env)
        else:
            if (len(sexpr) == 3):

                if carac == "print":

                    print(default_env()[carac](a,eval(b, env)))

                    return b
            return default_env()[carac](a,eval(b, env)) 
    if type(sexpr) == bool:

        return bool(sexpr)
    if type(sexpr) == int:
        
        return int(sexpr)
    
    else:
        return NotImplementedError


def compile_function(
    argdefs: ArgDefs, restype: type, body: SExpr, env: Env
) -> Callable:
  
    def fn():
        return 42

    return fn


def compile_module(ir: IR, env: Env) -> Dict[str, Callable]:
    """
    Compila um módulo a partir da IR e retorna um dicionário
    que relaciona o nome de cada função à sua implementação correspondente.

    Todas estas funções são espelhadas no dicionário de ambiente.
    """

    module = {}

    # Popula ambiente com definições de funções.
    # Cada declaração adiciona uma entrada (nome, função)
    # no dicionário de ambiente.
    for (name, define) in ir.items():
        args, restype, body = cast(tuple, define)
        func = compile_function(args, restype, body, env)
        module[name] = env[name] = func

    return module


def default_env():
  
    return {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "print": lambda x, y: x,
        "/": lambda x, y: x//y,
        "<": lambda x, y: x < y,
        "*": lambda x, y: x * y,
        "~": lambda x: not x,
        "=": lambda x, y: x == y,
        "|": lambda x, y: x or y,
        "^": lambda x, y: x^y,
        "if1": lambda x, y, z: y,
        "if2": lambda x, y, z: z,
        "|": lambda x, y: x,
        "|2": lambda x, y: not(x)
    }


# -----------------------------------------------------------------------------
# Funções auxiliares
#
# (implementações fornecidas, já que não tem nada de muito interessante para
# a matéria de compiladores)
# -----------------------------------------------------------------------------


def run_module(ir: IR) -> Value:
  

    env = default_env()
    module = compile_module(ir, env)

    # Lê argumentos da linha de comando e executa a função main
    # do ambiente
    argdefs = ir["main"][0]
    argvalues = read_args(argdefs)

    main_fn = cast(Callable, module["main"])
    result = main_fn(*argvalues)

    # Imprimimos true|false e não True|False, como acontece por padrão no Python
    if isinstance(result, bool):
        print("true" if result else "false")
    else:
        print(result)

    return result


def read_args(argdefs: ArgDefs) -> Iterator[Value]:
    """
    Lê argumentos do terminal a partir do padrão declarado em argdefs.
    """
    for k, typ in argdefs:
        while True:
            value = input(f"{k} ({typ.__name__}): ")

            if typ == int:
                try:
                    yield int(value)
                    break
                except ValueError:
                    print("ERRO: inteiro inválido!")

            elif typ == bool:
                if value == "true":
                    yield True
                    break
                elif value == "false":
                    yield False
                    break
                else:
                    print("ERRO: booleano inválido!")
