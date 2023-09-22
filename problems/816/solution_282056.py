def maiores(lista,inteiro):
    x=list.extend(lista,[inteiro])
    y=list.index(inteiro)
    h=list.sort(x)
    g=h[-1:3:-1]
    return g