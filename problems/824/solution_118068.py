def uppCons(frase):
    '''
    '''
    
    i=0
    frase2=''
    
    while i<len(frase):
        
         if frase[i] in 'QWERTYUIOPASDFGHJKLÇCVBNMZXaeiou':
                frase2+=.upper(frase[i])
         
         i+=1
    
    return frase2