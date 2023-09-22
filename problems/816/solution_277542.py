def maiores(lista,n):
    list.append(lista,n)
    list.sort(lista)
    posicao = list.index(lista,n)
    del lista[0:posicao]
    return lista