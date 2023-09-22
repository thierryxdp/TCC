def total(lista,d):
    a=list(dict.keys(d))
    for i in lista:
        p=list.index(a,i)
        h=d[p]
        return h