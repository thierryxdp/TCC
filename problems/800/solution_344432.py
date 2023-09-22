def total(lista,preco):
    v=0
    for c in lista:
        if c in list(dict.keys(produtos)):
            s+=produtos[c]
        else:
            v=v
    return round(v,2)