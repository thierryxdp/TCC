def fatorial(numero):
    '''
    Função que retorna o fatorial de um núemro após ele ser inserido na entrada
	int -> int
    '''
    numero>=0
    fatorial_resultante = 1
    contador = 1
    while contador <= numero:
    	fatorial_resultante = fatorial_resultante*contador
    	contador = contador + 1

	return fatorial_resultante