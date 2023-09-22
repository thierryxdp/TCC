def faltante(lista):
    list.sort(lista)
    i=0
    a=0
    d=i+1
    while i<len(lista):
        if lista[i]% d != 0:
            a = (lista[i] - 1)
        else:
            a = (len(lista) + 1)
        i += 1
    return a