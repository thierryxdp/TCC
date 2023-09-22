def faltante(lista):
    ""
    list.sort(lista)
    i = 0
    n = lista[i] - 1 
    while i < len(lista):
        if lista[i] == i+1:
            n = lista[i] + 1 
        i += 1
    return n