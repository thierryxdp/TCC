def filtra_pares (tup):
    '''Função que recebe uma tupla com 4 elementos inteiros
    como parâmetros e retorna uma nova tupla contendo os
    elementos pares da tupla original, na mesma ordem em
    que se encontravam'''
    return (n for n in tup if n % 2 == 0)