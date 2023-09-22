def posLetra(string,letra,n):
    c=0
    f=str.index(string,letra)
    while c<len(string):
        if string[c]==letra:
        c=c+1
            if f==n:
                return f
    return -1