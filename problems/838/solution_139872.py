def num_bombons (d,p):
    ''' funcao que calcula o numero maximo de bombons de preco p que se consegue comprar com a quantia d de dinheiro
	float, float -> int '''
    import math
    return math.floor (d/p)