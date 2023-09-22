def maiores(lista,n):
    i = 0
    while i < len(lista):
        if lista[i] < n:
            del lista[i]
    i = i + 1
    return lista