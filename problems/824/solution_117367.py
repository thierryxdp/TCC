def uppCons(frase):
    
    i=0
    
    frase=str.upper(frase)
    
    while i<len(frase):
        if frase[i] != 'A' or 'E' or 'I' or 'O' or 'U':
            novafrase=frase[i]
            i+=1
            
        else:
            i+=1
            
            
        return novafrase