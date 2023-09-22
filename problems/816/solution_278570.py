def maiores(lista, n):
    lista.append(n)
    lista.sort()
    posicao_n = lista.index(n)
    maiores_n = lista[posicao_n + 1:]

    return maiores_n