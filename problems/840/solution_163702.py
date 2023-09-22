import math
def bolos(farinha, ovo, leite):
    receita = ((farinha / 2) + (ovo / 3) + (leite / 5)) // 3
    if (farinha  / 2) < 1 and (ovo / 3) < 1 and (leite / 5) < 1:
            return 0
    else:
            return 'asda'
    return math.trunc(receita)