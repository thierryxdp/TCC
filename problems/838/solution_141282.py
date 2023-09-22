import math as m
def num_bombons(x,y):
	'''caulcula e retorna numero de bombom dado seu preco y e
    a quantia disponivel x
    float,float->int'''
	return m.floor(x/y)