def posLetra(string,letra,n):
    c=0
    l=0
    f=str.index(s,l)
    while c<len(s):
        if string[c]==l:
            if f==n:
                return f
        c=c+1
    return -1