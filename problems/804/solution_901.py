def filtra_pares(tup):
    '''filtra_pares : tuplo -> inteiro, inteiro, inteiro, inteiro
   recebe quatro tuplo de inteiros e devolve o numero de elementos pares na tupla'''
    if not (tup):
        return filtra_pares(tup[2:]