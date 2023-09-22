def maiores(lista,n):
    r=()
    for e in lista:
        if(lista[e]>n):
            r=r+[e,]
    return r