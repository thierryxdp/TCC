import math
def bolos(farinha, ovo, leite):
    receita = ((farinha / 2) + (ovo / 3) + (leite / 5)) / 3
    if farinha % 2 == 0 and ovo % 3 == 0 and leite % 5 == 0:
    	return math.trunc(receita)