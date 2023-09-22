def faltante(lista):
    pecas=list(range(1,lista[-1]+1))
    i=pecas[-1]
    while len(pecas)>=i:
        if pecas[i] in lista:
            i=i-1
        else:
            falta=pecas[i]
    return falta