def posLetra(s, l, n):
    o = 0
    for i in range(len(s)):
        if x == l:
            o += 1
        if o == n:
            return i
    return -1