def maiores(lista,n):
    r=[]
    for i in range(len(lista)):
        if lista[i] > n:
            r.append(lista[i])
            r.sort()
    return r