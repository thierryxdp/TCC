def filtra_pares(numeros):
    '''uma função que retorna uma tupla contendo apenas os elementos pares da tupla original.'''
    pares= ()
    if numeros[0] % 2 == 0:
        pares += (numeros[0],)
    if numeros[1] % 2 ==0:
        pares += (numeros[1],)
    if numeros[2] % 2 ==0:
        pares += (numeros[2],)
    if numeros[3] % 2 ==0:
        pares += (numeros[3])
        return pares