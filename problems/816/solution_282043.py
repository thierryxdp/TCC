def maiores(lista,inteiro):
    x=list.extend(lista,[inteiro])
    y=list.index(x,inteiro)
    h=list.sort(x)
    g=h[-1:y:-1]
    return g