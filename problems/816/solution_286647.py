def maiores(lista,n):
    list.sort(lista)
    if n in lista:
        del lista[0:list.index(lista,n)]
    else:
        if [n]<lista:
            lista=lista
        if [n]>lista:
            lista=[]
    return lista