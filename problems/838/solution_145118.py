import math
def num_bombons(d,p):
    """Calcula e retorna quantos bombons ele 
    consegue comprar, dados o dinheiro e o preço 
    do bombom para realização da compra.
    """
    return math.floor(d/p)