def faltante(lista):
    pecas=list(range(1,lista[-1]+1))
    n=0
    i=1
    falta=0
    while n<len(lista):
        if lista[i] in pecas:
            i=i+1
        else:
            falta=falta+i
    return falta