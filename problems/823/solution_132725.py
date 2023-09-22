def faltante (lpecas):
    '''identifica e retorna o valor numerico da peca faltante na lista;
    list -> int'''
    l = []
    x = 0
    lpecas.sort()
    while x < (len(lpecas)-1):
        if lpecas[x+1] - lpecas[x] > 1:
            return x + 2
        if lpecas[0] == 1:
            return lpecas[-1]+1
        if lpecas[1] == 2:
            return lpecas == 1
        else:
            return lpecas[0]-1