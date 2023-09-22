import math  
def boloS(A, B, C):
   """Calcular a quantidade de bolo"""

    farinha(A//2)
    ovos(B//3)
    leite(C//5)
    return math.min(farinha, ovos, leite)