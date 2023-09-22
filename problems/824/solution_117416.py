def uppCons(frase):
    
    i=0
    
    while i<len(frase):
        
        if frase[i]=='aeiou':
            i += 1
            
        else:
            x=str.upper(frase[i])
            str.replace(frase,frase[i],x,1)
            
            i += 1
            
            
        return frase