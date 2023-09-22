from math import *
def num_bombons (d,p):
	"""fornece o número de bombons que podem ser comprados dados o dinheiro "d"
    disponível e o preço unitário "P";
    int,int->float"""
    return c(d/p)