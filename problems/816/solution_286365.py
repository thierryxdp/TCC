def insere(lista_numero,n):
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero


def maiores(lista,n):
    i = 0
    lista_nova = insere(lista,n)
    indice = list.index(lista_nova,n)
    elemento = lista_nova[indice]
    while i != indice:
        del lista_nova[i]
        i += 1
    return lista_nova