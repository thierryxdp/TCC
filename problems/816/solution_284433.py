def maiores(lista, x):
    list.append(lista, x)
    list.sort(lista)
    for n in range(len(lista)):
        c = lista[n]
        if c <= x:
            list.remove(lista, lista[n])
    return lista