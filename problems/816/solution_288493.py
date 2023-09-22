def maiores(lista, numero):
    lista2 = []
    for x in lista:
        if x>numero:
            lista2.append(x)
    lista2.sort()
    return lista2