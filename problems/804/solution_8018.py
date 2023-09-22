def filtra_pares(numeros):
    """funcao que recebe uma tupla com 4 numeros inteiros e retorna apenas os numeros pares
    entrada: tuple
    saida: tuple"""
    pares = ()
    if numeros[0]%2==0:
        pares = pares + (numeros[0],)
    if numeros[1]%2==0:
        pares = pares + (numeros[1],)
    if numeros[2]%2==0:
        pares = pares + (numeros[2],)
    if numeros[3]%2==0:
        pares = pares + (numeros[3],)

    return pares