import math
def bolos(farinha, ovo, leite):
    receita = ((farinha / 2) + (ovo / 3) + (leite / 5)) // 3
    return math.trunc(receita)