def maiores(lista, numero):
    lista_maiores = []
    for elemento in lista:
        if elemento > numero:
            lista_maiores += [elemento]
    return list.sort(lista_maiores)