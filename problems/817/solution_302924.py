def maiores(lista,n):
    listan=[]
    list.sort(lista)
    for x in lista:
        if x>n:
            listan.append(x)
    return listan