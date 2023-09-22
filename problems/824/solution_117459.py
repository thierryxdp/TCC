def uppCons(frase):
    
    i=0
    
    vogais='aeiou'
    
    novafrase=''
    
    while i<len(frase):
        
        if frase[i] in vogais:
            
            novafrase+=frase[i]
            i += 1
        
        else:
      
            novafrase+=str.upper(frase[i])
            i += 1
            
            return novafrase