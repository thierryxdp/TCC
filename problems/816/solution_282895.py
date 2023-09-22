def maiores(lista,n):
    list.sort(lista,reverse=True)
    a=str(lista)
    p=str.partition(a,str(n))
    return p[0]