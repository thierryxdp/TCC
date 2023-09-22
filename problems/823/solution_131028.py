def faltante (lista):
    i = 0
    list.sort(lista)
    while i< len(lista):
        if lista[i]!=i+1:
            return i+1
        i = i+1
    return i+1