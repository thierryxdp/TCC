def posLetra(p,l,n):
    i=0
    posicao=-1
    while i<len(p):
        if l in p:
            posicao=str.index(p,l,n)
        return posicao