import math
def num_bombons(x,y):
    """ calcula o numero maximo de bombons que pedrinho pode comprar com o dinheiro(x) que possui dado o preço(y) do bombom """
    return math.floor(x/y)