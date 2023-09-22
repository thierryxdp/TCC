def maiores(x,n):
    x=x+[n]
    list.sort(x)
    return x[list.index(x,n)+1:]