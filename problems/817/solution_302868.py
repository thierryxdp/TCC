def acima_da_media(al, n=5):
    al.insert(-1, n)
    al.sort()
    al.reverse()
    x = al.index(n)
    al.remove(5)
    y = al[0:x+1]
    y.reverse()
    return y