def posLetra(s,l,n):
    x = 0
    for i in s:
        if s(i) == l:
            x += 1
        if x == n:
            return i
    return -1