def maiores(l,n):
    list.sort(l)
    f=list.index(l,n)
    if n in l:
        return f[n:]