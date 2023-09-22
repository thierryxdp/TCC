def uppCons(frase):
    
    i=0
    
    while i<len(frase):
        
        if frase[i] in 'aeiou':
            i += 1
            
            
        if frase[i] not in 'aeiou':
            x=str.upper(frase[i])
            str.replace(frase,frase[i],x,1)
            i += 1
            
        
            return frase