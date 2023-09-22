import math as m
def num_bombons(x,y):
	'''caulcula e retorna numero de bombom dado seu preco x e
    a quantia disponivel
    float,float->int'''
	return m.floor(y/x)