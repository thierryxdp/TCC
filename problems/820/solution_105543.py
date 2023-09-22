def posLetra(s, c, n):
    o = 0
    for i in range(len(s)):
        if s[i] == c:
            o += 1
        if o == n:
            return i
    return -1    def repetidos(l):
    n = 0
    for i in range(len(l)):
        if l[i] == l[i-1]:
            n +=1
    return n