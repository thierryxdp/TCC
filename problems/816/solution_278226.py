def maiores(lista,n):
    for x in insere(lista,n)[:list.index(lista,n)]:
        list.remove(lista,x)
    return lista