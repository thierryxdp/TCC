def maiores(lista,n):
    #list,int->list
    list.sort(lista)
    while lista[0]<=n:
        list.remove(lista,lista[0])
    return(lista)