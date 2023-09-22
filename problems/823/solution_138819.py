def faltante(lista):
    pecas=list(range(1,lista[-1]+1))
    i=1
    n=0
    falta=0
    while i<len(lista):
        if lista[n] in pecas:
            i=i+1
            n=n+1
        else:
            falta=lista[i]
    return falta