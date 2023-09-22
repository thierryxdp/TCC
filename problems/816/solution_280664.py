def maiores(lista, n):
    lista_maior = []
    for i in lista:
        if i > n:
            x = list.pop(lista)
            list.append(lista_maior, x)
    return lista_maior.sort()