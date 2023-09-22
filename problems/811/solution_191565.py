from math import *
def colchao(medidas,h,l):
	'''função que, dadas as medidas de um colchão e de uma porta,retorna um valor booleano
       que indica se o colchão passa pela porta ou não.
       list, int, int -> bool'''
    
    if medidas[0]<=min(h,l) and medidas[1]<=max(h,l):
        return True
    else:
        return False