def posLetra(string,letra,n):
    c=0
    f=str.index(string,letra)
    while c<len(string):
        if string[c]==letra:
            if string[c]==n:
                return 
        c=c+1
    return -1