def uppCons(frase):
    
    i = 0
    frase2 = ''
    
    while i<len(frase):
        if frase[i] in 'QWRTPSDFGHJKLÇZXCVBNMqwrtpsdfghjklçzxcvbnm':
            frase2 = frase2 + frase[i].upper()          
        else:
            frase2 = frase2 + frase[i]
            
            
        i = i+1
        
    return frase2