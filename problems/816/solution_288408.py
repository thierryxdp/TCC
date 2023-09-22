def maiores(ls,n):
    r = []
    for e in range(len(ls)):
        if ls[e] > n:
            r.append(ls[e])
            r.sort()
    return r