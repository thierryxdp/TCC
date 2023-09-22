def posLetra(s, c, n):
    o = 0
    for i in range(len(s)):
        if s[i] == c:
            o += n
        if o == n:
            return n
        
    return -1