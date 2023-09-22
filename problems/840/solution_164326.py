#exercicio 3

import builtins
from builtins import min 

def bolos(A,B,C):
    ''' calcula maxima quantidade de bolos possiveis, dado os ingredientes
      	 em casa (A -xicaras de farinha de trigo- B -ovos- e C -colheres 
         de sopa de leite)'''
    trigo = A//2
    ovo = B//3
    leite = C//5
    bolo = builtins.min(trigo,ovo,leite)
    return bolo;