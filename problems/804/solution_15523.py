def filtra_pares(a,b,c,d):
    '''Funçao que retorna os numeros pares dados 4 numeros
    inteiros na entrada
    Entrada: int, int, int, int
    Saida: tuple'''
    numeros = (a,b,c,d)
    pares = list(filter(lambda x: x%2==0, numeros))
    return (pares)