def maiores(lista1, n):
    list.insert(lista1, n, 0)
    list.sort(lista1)
    posicao_numero = list.index(lista1, n)
    lista_nova = lista1[posicao_numero:]
    return lista_nova