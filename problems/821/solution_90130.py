def fatorial(n):
    '''Cacula o fatorial de um numero.
    int --> int'''
    i = n
    k = 0
    resultado = 0
    while i > 0:
        resultado = resultado * (k+1)
        if i == n:
            resultado = 1
        i -= 1
        k += 1
	return resultado