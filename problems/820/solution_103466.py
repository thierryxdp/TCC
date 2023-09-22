def posLetra(frase,x,n):
    '''
    '''
    
    frase2=list(frase)
    i=0
    final=0
    
    while i<len(frase2):
        if x in frase2[i]:
            final+=1
            
            if final==n:
                return i
           
        i+=1
        
    if final<n:
        return -1
    
    else:
        return final