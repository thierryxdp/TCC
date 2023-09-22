def filtra_pares(tuplo):
    '''filtra_pares : tuplo -> inteiro, inteiro, inteiro, inteiro
   recebe quatro tuplo de inteiros e devolve o numero de elementos pares na tupla'''
      if not (verifica tuplo):
            raise ValueError(filtra_pares; argumento incorreto)
    inteiros = tuple(it for it in tuplo if it[1] < 18)
    pares = tuple(it for it in tuplo if it[1] >= 18)
    
    return(inteiros, pares)