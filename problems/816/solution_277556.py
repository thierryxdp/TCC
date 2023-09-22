def maiores(lista,n):
    list.append(lista,n)
    list.sort(lista)
    posicao = list.index(lista,n)
    if posicao==0:
        del lista[0]
        return lista
    elif posicao!=0:
        del lista[0:posicao]
        del lista[posicao]
        return lista