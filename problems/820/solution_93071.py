def posLetra(p,l,n):
    i=0
    while i<len(p):
        if l in p:
            if str.count(p,l)==1:
                posicao=str.find(p,l)
            if str.count(p,l)>1:
                if n==2:
                    posicao=str.find(p,l,str.find(p,l))
     return posicao