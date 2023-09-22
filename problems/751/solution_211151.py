def quant_palavras(frase):
    '''Retorna o número de palavras da frase.
    str --> int'''
    f = []
    f[:] = frase
    if len(f) == 0:
        return 0
    if ' ' == f[0]:
        del(f[0])
    if len(f) == 0:
        return 0
    if ' ' == f[-1]:
        del(f[-1])
    if len(f) == 0:
        return 0
    n = list.count(f,' ')
    return n+1