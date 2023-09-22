def posLetra(s,l,n):
    v=0
    o=0
    while v<len(s):
        if s[v]==l:
            o+=1
        if o==n:
            return v
        v+=1
    return -1