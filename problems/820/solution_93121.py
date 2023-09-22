def posLetra(s, l, n):
    i = 0
    c = 0
    if n > s.count(l):
        return -1
    while i <= len(s):
        if s[i] == l:
            c += 1
        if c == n:
            return i
        i += 1