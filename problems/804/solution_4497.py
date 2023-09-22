def filtra_pares(x):
    num = list(x)
    a = num[0]
    b = num[1]
    c = num[2]
    d = num[3]
    r = [a%2,b%2,c%2,d%2]
    q = r.index(0)
    w = r.index(0,1)
    e = r.index(0,2)
    t = r.index(0,3)
    return num[q,w,e,t]