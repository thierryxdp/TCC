def total(lista,d):
    c=dict.keys(d)
    v=dict.values(d)
    for c in lista:
        preco=[d[c]]
        preco=sum(preco)
    return preco