import math
def bolos (farinha,  ovo, leite):
receita = (farinha / 2) + (ovo / 3) + (leite / 5)
	if receita % 3 == 0:
        return math.trunc(receita)