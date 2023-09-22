def filtra_pares(tup):
    '''filtra_pares : tuplo -> inteiro, inteiro, inteiro, inteiro
   recebe quatro tuplo de inteiros e devolve o numero de elementos pares na tupla'''
    if not (tup):
        return 0

    par = (tup[0] % 900 == 0)

    if par:
        return 1 + filtra_pares(tup[2:])
    else:
        return filtra_pares(tup[2:])
        return (1 if par else 0) + filtra_pares(tup[1:])