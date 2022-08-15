from typing import MutableMapping, Optional

from .ir import IR

# O ambiente de execução é um dicionário mapeando nomes em valores
# que descrevem propriedades de cada variável.
Env = MutableMapping[str, object]


def optimize(ir: IR, env: Env = None) -> IR:
## nao deu :(
    return ir



def default_env() -> Env:
    """
    Retorna o ambiente de execução padrão.
    """
    return {}
