def maiores(x,n):
    list.append(x,n)
    list.sort(x)
    indice = list.index(x,n)
    del x[:(n+1)]
    return x