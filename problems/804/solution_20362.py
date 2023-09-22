def filtra_pares(x,y,z,a):
    '''analisa quais elementos inteiros da tupla: (x,y,z,a) são pares, e retorna aqueles correspondentes em ordem em uma nova tupla;
    tupla -> tupla'''
    pares = ()
    if x%2 == 0:
        pares = pares + (x,)
	if y%2 == 0:
        pares = pares + (y,)
    if z%2 == 0:
        pares = pares + (z,)
    if a%2 == 0:
        pares = pares + (a,)
    return pares