def faltante(lpeças):
    '''Identifica e retorna o valor numérico da peça faltante da lista.
    list -> int'''
    l = []
    x = 0
    lpeças.sort()
    while i < (len(lpeças)-1):
        if lpeças[x+1] - lpeças[x] > 1:
            return x + 2
        x += 1
    if lpeças[0] == 1:
        return lpeças[-1]+1
    else:
        return lpeças[0]-1