def maiores(lista, n):
    list.sort(lista)
    list.reverse(lista)
    lista2 = []
    num = list.pop(lista, 0)
    while num > n:
        lista2.append(lista)
    return lista2