def maiores(lista, n):
    list.sort(lista)
    ret=[]
    for elemento in lista:
        if( elemento > n ):
            list.append(ret, elemento)
    return ret