def total(lista,d):
    c=dict.keys(d)
    v=dict.values(d)
    i=0
    for c in lista:
        lista=lista[i]
        preco=d[lista]
        preco=preco+preco
    return preco