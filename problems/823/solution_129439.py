def faltante(lista):
    i = 0
    n = 1
    while list.sort(lista + [n]) != [*range(n)]:
        n = n + 1
    return n