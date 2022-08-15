from typing import Dict, Union, Tuple, List, NamedTuple
from lark import InlineTransformer, Tree
from lark.visitors import Transformer, v_args

IR = Dict[str, "Declaration"]

Declaration = Tuple["ArgDefs", type, "SExpr"]

ArgDefs = List[Tuple[str, type]]

SExpr = Union[list, str, int, bool]


def transform(tree: Tree) -> IR:
   transf = TransformerClass()
   return transf.transform(tree)

class Declaration(NamedTuple):
    args: List[Tuple[str, type]] ## arg
    principal: SExpr
    returns: str


class TransformerClass(Transformer):

      ## define true
      def true(self):
         return True
     ## define false
      def false(self):
         return False
     ## define inteiro
      def INTEGER(self, p):
         return int(p)
     ##define bool 
      def BOOLEAN(self, children):
         if (children == "false"):
            return False
         elif (children == "true"):
            return True
        ## identificador
      def IDENTIFIER(self, p):
         return str(p)

        #ou
      @v_args(inline=True)
      def or_(self, a, b):
         return ['|', a, b]
     #add
      @v_args(inline=True)
      def add(self, a, b):
         return ['+', a, b]
     #sub
      @v_args(inline=True)
      def sub(self, a, b):
         return ['-', a, b]

     #div
      @v_args(inline=True)
      def div(self, a, b):
         return ['/', a, b]
   
      @v_args(inline=True)
      def and_(self, a, b):
         return ['^', a, b]
   
      @v_args(inline=True)
      def mul(self, a, b):
         return ['*', a, b]


     #igual
      @v_args(inline=True)
      def eq(self, a, b):
         return ['=', a, b]

     #lt
      @v_args(inline=True)
      def lt(self, x, y):
         return ['<', x, y]

      #bool ou int
      def TYPE(self, carac):
            if(carac == "boolean"):
               return bool
            else:
               return int

    #condicao definida
      @v_args(inline=True)
      def cond(self, pri, seg, terc):
          return ["if", pri, seg, terc]
      
      #inteiro
      def integer(self):
         return int

      @v_args(inline=True)
      def param(self, name, p_type):
         if type(p_type) == str:
            p_type = self.TYPE(p_type)
         return (str(name),p_type)
      
      def params(self, raiz):
         return raiz

      def args(self, raiz):
         return raiz
       #chamada de função
      @v_args(inline=True)
      def fcall(self, id, argmap):
         vet = []
         vet.append(id)
         for i in argmap:
            vet.append(i)
         return vet
      

      def principal(self, imprime_exp):
         vet = []
         for i in imprime_exp:
            if(tuple==type(i)):
              for x in i: 
               vet.append(x)
            else:
               vet.append(i)
         return vet



      def imprime_exp(self, raiz):
         vet = []
         vet.append("print")
         for i in raiz:
            vet.append(i)
         return tuple(vet)


      def exp(self, exp):
         return exp
      

      def program(self, def_list):
         mapa={} 
         for i in def_list:
               key=i[0]
               val=i[1]
               mapa[key]=val
         return mapa



      @v_args(inline=True)
      def define(self, name, params, type, principal):

         return [name, Declaration(params, type, principal)]

