def faltante(lista):
    list.sort(lista)
    i=0
    a=0
    while i<len(lista):
        if lista[i]%(i+1) != 0:
            a += lista[i]
        i += 1
    return a