from typing import List, MutableMapping, Any
from .ir import IR


SemanticError = str

ERROR_NO_MAIN = "Programa não define a função 'main'."
ERROR_TYPES = "O verificador de tipos encontrou um erro."

Env = MutableMapping[str, Any]

def semantic_analysis(ir: IR, env: Env) -> List[SemanticError]:
    if ir.get("main"):
        return []  
    else:
        return [ERROR_NO_MAIN]