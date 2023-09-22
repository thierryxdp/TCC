def filtra_pares(a,b,c,d):
    """Dados 4 numeros inteiros essa funcao retorna os numeros pares dentro
    desses 4 numeros
    """
    numeros = [a,b,c,d]
    saida = list(filter(lambda x: x%2 == 0, numeros))
    return saida