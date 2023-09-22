def filtra_pares(tupla):
    '''Retorna uma tupla contendo os elementos pares
    de uma tupla, com quatro numeros inteiros, dada;
    tuple -> tuple'''
    pares = ()
    for numero in tupla:
        if numero % 2 == 0:
            pares += (numero,) 
    return pares