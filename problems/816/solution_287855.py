def maiores(l,n):
    #
    l.append(n)
    l2=sorted(l)
    l2+l2[l2.index(n):]
    l2.remove(n)
    return l2