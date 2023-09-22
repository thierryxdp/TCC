def posLetra(s, l, n):
    x = 1
    c = 0
    while x < n:
        if l in s:
            s = s[s.index(l): ]
    return s.index(l)