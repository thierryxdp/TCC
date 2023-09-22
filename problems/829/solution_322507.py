import math
def soma_h(n):
    """ """
    """ """
    soma = 0
    for i in range(1, n + 1):
        inverso = (1/i)
        soma += inverso
    return round(soma, 2)