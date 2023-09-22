def maiores(ls,x):
    list.sort(ls)
    pos=list.index(ls,x)
    return ls[pos+1:]