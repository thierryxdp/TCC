def posLetra(string,letra,n):
    c=0
    l=0
    f=str.index(string,l)
    while c<len(string):
        if string[c]==letra:
            if f==n:
                return f
        c=c+1
    return -1