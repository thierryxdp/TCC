def maiores(x,n):
    list.insert(x,0,n)       
    list.sort(x)
    return x[(list.index(n)+1)::]