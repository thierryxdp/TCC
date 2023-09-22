def faltante(lista):
    pecas= len(lista)+1
    lista.sort()
    i=0
    while i < pecas-1:
        if lista[i] != i:
            return i
        else:
            i += 1