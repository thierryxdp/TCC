def posLetra(string,letra,n):
    tam=len(string)
    c=0
    c1=0
    
    while c<tam:
        if string[c]==letra:
        	c1=c1+1
            
        if c1==n:
            break
        
        c += 1
        
    if c1<n:
        return -1
    return c