def maiores(lista,n):
    ''''''
    list.sort(lista)
    pn=list.index(lista,n)
    listaf=lista[pn+1,]
    return listaf