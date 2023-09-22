def posLetra(s, l, n):
    c = []
    for i in s:
        if i == l:
            c.append(s.index(i)) 
    if len(c) < n:
        return -1
    if len(c) >= n:
        return c[-1]