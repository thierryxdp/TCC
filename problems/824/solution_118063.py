def uppCons(frase):
    '''
    '''
    
    i=0
    frase2=''
    
    while i<len(frase):
        
         if frase[i] in 'aABCDeEFGHiIJKLMNoOPQRSTuUVWXYZ':
                frase2=frase2+frase[i]
         
         i+=1
    
    return frase2