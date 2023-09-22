def posLetra(s,l,n):
    i = 0
    r = 0
    while i < len(s):
        if s[i] == l:
            r = r + 1
            if r == n:
                return i
        i = i +1
    if r < n:
        return -1