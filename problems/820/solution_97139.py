def posLetra(s,letra,n):
    prox=0
    if s[letra,n] not in letra:
        return -1
    while prox<len(s):
        if s[prox]==letra:
            return s.index(letra,n)          
        prox=prox+1