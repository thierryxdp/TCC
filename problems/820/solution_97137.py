def posLetra(s,letra,n):
    prox=0
    while prox<len(s):
        if s[prox]==letra:
            return s.index(letra,n)          
        prox=prox+1
    return -1