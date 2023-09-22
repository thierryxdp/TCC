def maiores(lista,n):
    if lista[0] < n:
        lista.remove(lista[0])
    elif lista[1] < n:
        lista.remove(lista[1])
    elif lista[2] < n:
        lista.remove(lista[2])
    elif lista[3] < n:
        lista.remove(lista[3])
    lista.sort()
    return lista