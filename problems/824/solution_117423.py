def uppCons(frase):
    
    i=0
    
    vogais='aeiou'
    
    while i<len(frase):
        
        if frase[i] in vogais:
            i += 1
            
            
        if frase[i] not in vogais:
            x=str.upper(frase[i])
            str.replace(frase,frase[i],x,1)
            i += 1
            
        
            return frase