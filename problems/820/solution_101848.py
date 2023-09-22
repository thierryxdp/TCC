def posLetra(s, l, n):
    c = []
    for i in s:
        if i == l:
            c.append(s.index(l))
        else:
            pass 
    if c.length() < n:
        return -1
    if c.length() >= n:
        return c[-1]