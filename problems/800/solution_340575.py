def total(lista,d):
    a=lista[0]
    b=lista[1]
    c=lista[2]
    h=lista[3]
    e=lista[4]
    f=lista[5]
    if len(lista)==6:
        preco=(d[a]+d[b]+d[c]+d[h]+d[e]+d[f])
        return preco
    elif len(lista)==4:
        preco=(d[a]+d[b]+d[c]+d[h])
        return preco