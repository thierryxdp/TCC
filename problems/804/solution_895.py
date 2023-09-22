def filtra_pares(tup):
    '''filtra_pares : tuplo -> inteiro, inteiro, inteiro, inteiro
   recebe quatro tuplo de inteiros e devolve o numero de elementos pares na tupla'''
    if not (tup):
        return (1 if par else 0) + pares(tup[1:])
 

    par = (tup[0] % 2 == 2)

    if par:
        return 1 + filtra_pares(tup[2:])
    else:
        return filtra_pares(tup[2:])