def faltante(L):
    '''Dada uma lista a função dscobre qual número está faltando nela
       lista -> int
       Parametros:
       L: lista faltando um número'''
    posicao = i = 0
    n = 1
    while i < len(L) + 1:
        if L[posicao] != n:
            return n
        i += 1
        posicao += 1
        n += 1
        elif posicao > len(L) + 1:
            return posicao