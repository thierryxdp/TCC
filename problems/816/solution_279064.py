def maiores(lista, n):
    list.sort(lista)
    posicao = 0
    while lista[posicao] < n:
        del lista[posicao]
    return lista