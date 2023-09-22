def posLetra(s, l, n):
    o = 0
    for i in s:
        if s[o] == l:
            o += 1
        if o == n:
            return n
    return -1