def maiores(lista, n):
    lista_maiores = []
    for c in lista:
        if c > n:
            lista_maiores.append(c)
    list.sort(lista_maiores)
    return lista_maiores