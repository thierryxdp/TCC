def substitui(s,x,i):
    l= list(s)
    l[int(i)] = str(x)
    s = "".join(l)
    return s