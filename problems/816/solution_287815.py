def maiores(l,n):
    list.sort(l)
    if n in l:
        f=list.index(l,n)
        return l[f:]