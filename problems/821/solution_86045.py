def fatorial(numero):
	'''Função que dado um número, calcula o fatorial do mesmo.
	Entrada: int
	Saída: int'''
    fatorial = 1
    parametro = 2

    while parametro <= numero:
        fatorial = fatorial*parametro
        parametro = parametro + 1

    return fatorial