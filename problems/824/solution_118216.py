def uppCons(frase):
    '''
    '''
    
    i=0
    frase2=list(frase)
    final=[]
    
    while i<len(frase2):
        if frase2[i] in 'cbdfghjklmnpqrstvwxyzç':
            final.insert(i,frase2[i].upper())
            
    i+=1
    
        else:
            
            final.insert(i,frase2[i])
            
    i+=1
    
    
    return final