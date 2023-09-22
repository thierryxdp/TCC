def maiores(lista,n):
    r=[]
    for i in lista:
        if lista[i] > n:
            r = r+lista[i]
            r.sort()
    return r