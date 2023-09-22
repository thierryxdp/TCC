def posLetra(frase,l,n):
    
    i=0
    a=list(range(n))
    
    while i<len(a):
        if frase[len(a)-1]==l:
            posicao=len(a)-1
            
            i=i+1
        else:
            posicao=-1
            
            i=i+1
    
    return posicao