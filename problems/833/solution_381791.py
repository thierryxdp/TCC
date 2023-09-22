def conta_numero(n, m):
    '''Dado um número e uma matriz, a função retorna quantas vezes
       tal número aparece na matriz
       int, list -> int
       Parametros:
       n: número inteiro
       m: matriz a ser digitada'''
    i = 0
    for c in range(0, len(m)):
        i += m[c].count(n)
    return i