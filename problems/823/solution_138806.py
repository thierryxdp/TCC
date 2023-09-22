def faltante(lista):
    pecas=list(range(1,lista[-1]))
    i=1
    falta=0
    while i<len(lista):
        if i in pecas:
            i=i+1
        else:
            falta=falta+i
            i=i+1
    return falta