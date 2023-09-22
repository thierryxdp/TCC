def num_bombons (d,p):
    ''' funcao que calcula o numero maximo de bombons de preco p a ser comprado com a quantia d de dinheiro
	float, float -> int '''
	from math import floor
	return floor (d/p)