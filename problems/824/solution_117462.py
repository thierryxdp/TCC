def uppCons(frase):
    
    i=0
    
    novafrase=''
    
    while i < len(frase):
        
        if frase[i] in 'aeiou':
            
            novafrase += frase[i]
            i += 1
        
        else:
      
            novafrase+=str.upper(frase[i])
            i += 1
            
            return novafrase