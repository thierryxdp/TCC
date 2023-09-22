def filtra_pares(elementos):
    '''analisa quais elementos inteiros da tupla: (x,y,z,a) são pares, e retorna aqueles correspondentes em ordem em uma nova tupla;
    tupla -> tupla'''
    pares = ()
    if elementos[0]%2 == 0:
        pares = pares + (elementos[0],)
	if elementos[1]%2 == 0:
        pares = pares + (elementos[1],)
    if elementos[2]%2 == 0:
        pares = pares + (elementos[2],)
    if elementos[3]%2 == 0:
        pares = pares + (elementos[3],)
    return pares