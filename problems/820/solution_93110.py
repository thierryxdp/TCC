def posLetra(s, l, n):
    i = 0
    i0 = 0
    while i <= len(s):
        if s[i] == l:
            i0 += 1
        if i0 == n:
            break
        if i0 < n:
            return -1
        i += 1
    return i