def acima_da_media(l, n=5):
    l.insert(-1, n)
    l.sort()
    l.reverse()
    x = l.index(n)
    y = l[0:x]
    y.reverse()
    return y