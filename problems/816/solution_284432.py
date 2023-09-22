def maiores(lista, x):
    list.append(lista, x)
    list.sort(lista)
    for n in range(len(lista)):
        if lista[n] <= x:
            list.remove(lista, lista[n])
    return lista