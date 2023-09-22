def faltante(lista):
    pecas=len(lista)+1
    lista.sort()
    i=0
    while i<pecas:
        if lista.range[i]!=i+1:
            return i+1
        i=i+1