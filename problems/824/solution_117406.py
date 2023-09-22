ef uppCons(frase):
    
    i=0
    
    while i<len(frase):
        
        if frase[i] == 'aeiou':
            i += 1
            
        else:
            str.upper(frase[i])
            i += 1
            
            
        return frase