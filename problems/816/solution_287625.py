def maiores(lista, n):
    for x in range(len(lista)):
        if lista[x] > n:
            lista.append(lista[x])
        return list.sort(lista)