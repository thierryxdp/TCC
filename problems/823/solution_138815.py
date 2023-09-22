def faltante(lista):
    pecas=list(range(1,lista[-1]+1))
    i=0
    falta=0
    while i<=len(lista):
        if lista[i] in pecas:
            i=i+1
        if lista[i] not in pecas:
            falta=i
    return falta