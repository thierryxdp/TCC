def acima_da_media(al, n=7):
    al.insert(-1, n)
    al.sort()
    al.reverse()
    x = al.index(n)
    y = al[0:x]
    y.reverse()
    return y