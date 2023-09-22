def posLetra(s, c, n):
    o = 0
    for i in range(len(s)):
        if s[i] == c:
            o += 1
        if o == n:
            return i
    return -1