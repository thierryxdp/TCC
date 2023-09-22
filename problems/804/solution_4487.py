def filtra_pares(a,b,c,d):
    num = [a,b,c,d]
    r = [a%2,b%2,c%2,d%2]
    q = r.index(0)
    w = r.index(0,1)
    e = r.index(0,2)
    t = r.index(0,3)
    return num[q,w,e,t]