def maiores(ls,n):
    list.sort(ls)
    k=list.index(ls,n)
    return ls[k+1:]