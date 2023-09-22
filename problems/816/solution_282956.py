def maiores(lista,n):
    if n in lista:
        list.sort(lista,reverse=True)
        a=str(lista)
        b=str.strip(a,'[')
        c=str.strip(b,' ' ')
        p=str.partition(c,str(n))
        return p
    else:
        list.append(lista,n)
        list.sort(lista,reverse=True)
        a=str(lista)
        b=str.strip(a,'[')
        c=str.strip(b,' ' ')
        p=str.partition(c,str(n))
        return p