def maiores(ls,n):
    list.sort(ls)
    pos=list.index(ls,n)
    return ls[pos+1:]