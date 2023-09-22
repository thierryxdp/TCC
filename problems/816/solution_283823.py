def maiores(lista,n):
    lista=list.sort(lista)
    posicao=list.index(lista,n)
    return lista[posicao:]