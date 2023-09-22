def maiores(ni,n):
    ni.append(n)
    y = sorted(ni)
    a = y.index(n)
    return y[a+1:]