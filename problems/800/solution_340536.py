def total(lista,d):
    c=dict.keys(d)
    v=dict.values(d)
    i=0
    for c in lista:
        lista=lista[i]
        i=i+1
        preco=d[lista]
        preco=float(sum(preco))
    return preco