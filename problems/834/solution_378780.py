import math

def media_matriz(m):
    ''' Retorna a media de todos os elementos de m'''
    c = 0
    k = 0
    for l in m:
        c += sum(l)
        k += len(l)
    media = math.floor(100*c/k)/100
    return media