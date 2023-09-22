def faltante(lista):
    list.sort(lista)
    i=0
    a=0
    while i<len(lista):
        if lista[i]%(i+1) != 0:
            a += (lista[i] - 1)
        else:
            a += (len(lista) + 1)
        i += 1
    return a