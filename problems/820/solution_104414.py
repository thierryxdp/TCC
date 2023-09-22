def posLetra(s,l,n):
    x = 0
    for i in s:
        if s.count (l) == n:
            x += 1
        if x == n:
            return i
    return -1