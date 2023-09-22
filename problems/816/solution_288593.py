def maiores(lista,n):
    l=[]
    for x in lista:
        if x>n:
            l.append(x)
    l.sort()
    return l