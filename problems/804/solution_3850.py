def filtra_pares(numeros):
    '''funçao que dada uma tupla com 4 numeros, retorna apenas os pares'''
    pares = ()
    if int(numeros[0])%2 == 0:
        pares += (numeros[0],)
    if int(numeros[1])%2 == 0:
        pares += (numeros[1],)
    if int(numeros[2])%2 == 0:
        pares += (numeros[2],)
    if int(numeros[3])%2 == 0:
        pares += (numeros[3],)
    return pares