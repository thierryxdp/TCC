def posLetra(string,letra,n):
    l=0
    t=''
    q=str.count(string,letra,)
    while l<len(string):
        if string[l]==letra:
            if str.find(string,letra,)==n:
                return l
        l=l+1
    return l