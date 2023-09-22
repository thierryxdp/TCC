def maiores(lista, limite):
    list.insert(lista, 0, limite)
    list.sort(lista)
    posicao = list.index(lista, limite)
    return lista[posicao+1:]