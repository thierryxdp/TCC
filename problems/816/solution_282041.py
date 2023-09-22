def maiores(lista,inteiro):
    x=list.extend(lista,[inteiro])
    y=list.sort(x)
    h=list.index(y,INT)
    g=y[-1:h:-1]
    return g