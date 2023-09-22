def posLetra(frase,x,n):
    '''
    '''
    
    frase2=list(frase)
    i=0
    final=''
    
    while i<len(frase2):
        if x in frase2[i]:
            frase2.count(x)
            final.join(frase2[i])
        
        i+=1
        
    return ''.join(final)