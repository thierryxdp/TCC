def maiores(lista,n):
    #list,int->list
    list.sort(lista)
    sair = len(lista)
    while sair>0:
        if lista[0]<=n:
            list.remove(lista,lista[0])
            sair = len(lista)
        else:
            sair = 0
    return(lista)