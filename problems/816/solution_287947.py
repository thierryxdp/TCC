def maiores(ls,n):
    r=[]
    for e in ls:
        if e > n:
            r.sort(e)
    return r