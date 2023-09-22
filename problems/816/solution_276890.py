def maiores(x,n):
    list.insert(x,0,n)
    list.sort(x)
    a=list.index(x,n)
    return x[a+1:]