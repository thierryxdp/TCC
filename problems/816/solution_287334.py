def maiores(lista,n):
    """ """
    listafinal=[]
    list.append(lista,n)
    for x in range(len(lista)):
        if lista[x] > n:
            listafinal.append(lista[x])
    return sorted(listafinal)