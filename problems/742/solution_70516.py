def substitui(s,x,i):
    a = list(s)
    a[i] = x
    z = ''
    for i in a:
        z = z+i
    return z