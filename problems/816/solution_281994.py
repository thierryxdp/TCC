def maiores(lista,INT):
    x=list.extend(lista,INT)
    y=list.sort(x)
    h=list.index(y,INT)
    g=y[-1:h:-1]
    return g