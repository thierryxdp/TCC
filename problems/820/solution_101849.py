def posLetra(s, l, n):
    c = []
    for i in s:
        if i == l:
            c.append(s.index(l))
        else:
            pass 
    if c.len() < n:
        return -1
    if c.len() >= n:
        return c[-1]