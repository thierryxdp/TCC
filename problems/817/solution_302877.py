def acima_da_media(al, n=5):
    al.insert(-1, n)
    al.sort()
    al.reverse()
    x = al.index(n)
    y = al[0:x]
    y.remove(5)
    y.reverse()
    return y