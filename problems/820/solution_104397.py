def posLetra(s,l,n):
    x = 0
    for y in s:
        if s[y] == l:
            x += 1
        if x == n:
            return y
    return -1