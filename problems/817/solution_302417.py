def acima_da_media(lista):
    n=sum(lista)/len(lista)
    return maiores(lista,n)






def maiores(lista,n):
    listan=[]
    list.sort(lista)
    for x in lista:
        if x>n:
           listan.append(x)
    return listan