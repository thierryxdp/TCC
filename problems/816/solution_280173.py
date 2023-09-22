def maiores(lista, n):
    i = 0
    while i <= len(lista):
        if lista[i] <= n:
            list.remove(lista, lista[i])
        i += 1
    
    return lista