def posLetra(s, l, n):
    o = 0
    for i in l:
        if s[i] == l:
            o += 1
        if o == n:
            return i
    return -1