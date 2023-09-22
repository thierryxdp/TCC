def fatorial(numero):
    '''Retorna o fatorial de um número n
    int-->int'''
    resultado=1
	count=1

	while count <= numero:
    	resultado *= count
    	count += 1
	return resultado