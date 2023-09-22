def maiores(lista, n):
    list.sort(lista)
    list.reverse(lista)
    lista2 = []
    while lista > n:
        lista2.append(lista)
    return lista2