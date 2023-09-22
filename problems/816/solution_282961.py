def maiores(lista,n):
    if n in lista:
        list.sort(lista,reverse=True)
        a=str(lista)
        b=str.strip(a,'[')
        c=str.strip(b,' ')
        p=str.partition(c,str(n))
        return str.split(p[0])
    else:
        list.append(lista,n)
        list.sort(lista,reverse=True)
        a=str(lista)
        b=str.strip(a,'[')
        c=str.strip(b,' ')
        p=str.partition(c,str(n))
        return str.split(p[0])