def carros(pessoas,lugares=5):
	'''
    Funçao que calcula quantos veiculos precisam para uma viagem
    utilizando o numero de pessoas que vao e o numero de lugares disponiveis
    int, int -> int
    '''
    import math
    n=pessoas/lugares
    c=math.ceil(n)
    return c