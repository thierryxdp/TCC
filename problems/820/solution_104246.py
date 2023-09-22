def posLetra(s, l, n):
    o = 0
    t=str.count(s)
    for i in t :
        if s[i] == l:
            o += 1
        if o == n:
            return i
    return -1