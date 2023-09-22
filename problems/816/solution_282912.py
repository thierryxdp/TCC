def maiores(lista,n):
    if n in lista:
        list.sort(lista,reverse=True)
        a=str(lista)
        p=str.partition(a,str(n))
        return p[0]
    else:
        list.append(lista,n)
        list.sort(lista,reverse=True)
        a=str(lista)
        p=str.partition(a,str(n))
        return p[0]