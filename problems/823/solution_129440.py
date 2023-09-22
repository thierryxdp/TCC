def faltante(lista):
    n = 1
    i = len(lista) + 1
    while list.sort(lista + [n]) != [*range(i)]:
        n = n + 1
    return n