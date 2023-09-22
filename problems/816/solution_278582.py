def maiores(lista, n):
    lista_maiores = [n]

    for i in lista:
        if i >= n:
            lista_maiores.append(i)

    return lista_maiores