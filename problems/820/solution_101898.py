def posLetra(p,l,n):
    i = 0
    a = 0
    if str.count(p,l) < n:
        return -1
    else:
        while str.find(p,l,i) != n:
            str.find(p,l,i)
            i += 1
        a = str.find(p,l,i) + 1
    return a