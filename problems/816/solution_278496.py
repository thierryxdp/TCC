def maiores(x,n):
    list.insert(x,n,0)       
    list.sort(x)
    return x[(list.index(n)+1)::]