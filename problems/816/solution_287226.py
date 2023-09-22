def maiores(lista,n):
    v=[]
    list.sort(lista)
    for x in lista :
        if x>n:
            v=v+[x,]
    return v