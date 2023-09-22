import math
def carros(n,nc):
    "funcao que calcula o numero de carros necessarios para uma viagem dado o numero de pessoas n e o numero de pessoas que cabem nos carros nc"
	return math.ceil(n/nc)