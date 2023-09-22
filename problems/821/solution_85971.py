def fatorial(numero):
    '''Dado um numero, a função retorna o calculo fatorial deste numero.
    	int -> int'''
    i = 2
    fatorial = 1
    while i <= numero:
        fatorial = fatorial*i
    	i = i + 1
	return fatorial