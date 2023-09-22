def carros (p, c=5):
    x = p/c
    y = p//c
    z = p%c
    if z==0:
        print (y)
    else:
        q = max(x, y+1)
        return q