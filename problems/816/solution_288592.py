def maiores(lista,n):
    l=[]
    for x in lista:
        if x>n:
            l.append(x)
    return l.sort()