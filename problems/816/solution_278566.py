def maiores(lista, n):
    posicao_n = lista.index(n)
    lista.sort()
    lista[:posicao_n + 1] = []

    return lista