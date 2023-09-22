def maiores(lista,n):
    r=[]
    for i in lista:
        if lista[i] > n:
            r.append(lista[i])
            r.sort()
    return r