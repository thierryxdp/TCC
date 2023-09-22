def carros(pessoas,capacidade=5)
	'''Calcula quantos carros são necessários para transportar determinada quantidade de pessoas'''
	(int,int=>int)
    automoveis=math.ceil(pessoas/capacidade)
    return automoveis