def carros(pessoas,lugares=5)
	'''
    Funçao que calcula quantos veiculos precisam para uma viagem
    utilizando o numero de pessoas que vao e o numero de lugares disponiveis
    int, int -> int
    '''
    n=pessoas/lugares
    c=ceil(n)
    return c