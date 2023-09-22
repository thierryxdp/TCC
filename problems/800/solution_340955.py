def total(lista,d):
    a=list(dict.keys(d))
    for i in lista:
        p=list.index(a,i)
        preco=d[p]
        return preco