def maiores(lista,n):
    list.append(lista,n)
    list.sort(lista)
    posicao = list.index(lista,n)
    if posicao==0:
        del lista[0]
        return lista