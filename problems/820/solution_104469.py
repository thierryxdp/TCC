def posLetra(s, c, n):
    o = 0
    for i in range(len(s)):
        if s[i] == c:
            o += n
        if o == c:
            return n
        
    return -1