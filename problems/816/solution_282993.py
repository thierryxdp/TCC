def maiores(lista,n):
    if n in lista:
        list.sort(lista)
        a=str(lista)
        b=str.strip(a,'[')
        c=str.strip(b,' ')
        p=str.partition(c,str(n))
        return str.split(p[2])
    else:
        list.append(lista,n)
        list.sort(lista)
        a=str(lista)
        b=str.strip(a,'[')
        c=str.strip(b,' ')
        p=str.partition(c,str(n))
        return str.split(p[2])