def maiores(lista,n):
    lista=list.sort(lista)
    posicao=lista.index(lista,n)
    return lista[posicao:]