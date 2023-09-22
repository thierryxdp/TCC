def faltante(lista):
    pecas=list(range(1,lista[-1]+1))
    i=0
    falta=0
    while i<len(pecas):
        if lista[i] in pecas:
            i=i+1
        else:
            falta=lista[i]
    return falta