import math
def bolos(farinha, ovo, leite):
    receita = ((farinha / 2) + (ovo / 3) + (leite / 5)) / 3
    if receita % 3 == 0 :
   		return (receita)
    else:
        return 'ok'