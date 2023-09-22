def faltante(lpecas):
    '''Identifica e retorna o valor numérico da peça faltante da lista.
    list -> int'''
    l = []
    x = 0
    lpecas.sort()
    while i < (len(lpecas)-1):
        if lpecas[x+1] - lpecas[x] > 1:
            return x + 2
        x += 1
    if lpecas[0] == 1:
        return lpecas[-1]+1
    else:
        return lpecas[0]-1