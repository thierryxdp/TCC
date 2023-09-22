def faltante(lista):
    list.sort(lista)
    i = 0
    n = 1
    while i<len(lista):
        if lista[i] == n:
            n = n + 1
        i = i + 1
    return n