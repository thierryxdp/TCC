def maiores(lista,n):
    if lista[0] < n:
        lista.remove(lista[0])
    elif lista[1] < n:
        lista.remove(lista[1])
    elif lista[2] < n:
        lista.remove(lista[2])
    elif lista[3] < n:
        lista.remove(lista[3])
    elif lista[4] < n:
        lista.remove(lista[4])
    elif lista[5] < n:
        lista.remove(lista[5])
    elif lista[6] < n:
        lista.remove(lista[6])
    elif lista[7] < n:
        lista.remove(lista[7])
    lista.sort()
    return lista