def faltante(lista):
    pecas= len(lista)+1
    lista.sort()
    i=0
    while i < pecas-1:
        if i not in lista:
            return i
        if lista[i] != i+1:
            return i+1
        else:
            i += 1