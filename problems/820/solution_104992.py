def posLetra(s, l, n):
    o = 0
    for i in s:
        if s[o] == l:
            o += 1
        if o == n:
            return o
        if o<n:
            return -1
           
    return -1