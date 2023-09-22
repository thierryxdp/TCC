def posLetra(s,x,n):
    o=0
    for i in range(len(s)):
        if s[i] ==l:
            o=o+1
        if o ==n:
            return i
    return -1