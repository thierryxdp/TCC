def maiores(lista,n):
    nova_lista=lista+[n]
    list.sort(nova_lista)
    posicao=list.index(nova_lista,n)
    return nova_lista[posicao+1:]