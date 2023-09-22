def posLetra(string,letra,n):
    size=len(string)
    c=0
    c1=0
    
    while c<size:
        if string[c]==letra:
        	c1=c1+1
            
        if c1==n:
            break
        
        c=c1+1
        
    if c1<n:
        return -1
    return c