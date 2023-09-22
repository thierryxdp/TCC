def uppCons(frase):
    '''
    '''
    
    i=0
    frase2=''
    
    while i<len(frase):
        
         if frase[i] in 'QWERTYUIOPASDFGHJKLÇCVBNMZXaeiou':
                frase2+=frase[i]
         
         i+=1
    
    return frase2