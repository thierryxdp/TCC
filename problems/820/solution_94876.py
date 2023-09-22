def posLetra(string,letra,n):
    l=0
    q=str.count(string,letra,)
    while l<len(string):
        if string[l]==letra:
            if l==n:
                return l
        l+1
    return l