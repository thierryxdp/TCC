def posLetra(p,l,n):
    i=0
    while i<len(p):
        if l in p:
            posicao=str.index(p,l,n)
        else:
            posicao=-1
        return posicao