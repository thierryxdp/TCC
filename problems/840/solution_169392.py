import math  
def bolos(A, B, C):
   """Calcular a quantidade de bolo"""

    qtd_trigo = math.floor(A//2)
    qtd_ovos = math.floor(B//3)
    qtd_leite = math.floor(C//5)

    igrediente = math.min(qtd_trigo, qtd_ovos, qtd_leite)
    return igrediente