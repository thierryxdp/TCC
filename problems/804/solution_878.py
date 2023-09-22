def filtra_pares(tup):
    '''filtra_pares : tuplo -> inteiro
   recebe tuplo de inteiros e devolve o numero de elementos pares na tupla'''
    if not (tup):
        return 0

    par = (tup[0] % 2 == 0)

    if par:
        return 1 + pares(t[1:])
    else:
        return pares(t[1:])