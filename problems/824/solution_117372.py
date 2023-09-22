def uppCons(frase):
    
    i=0
    
    while i<len(frase):
        
        if frase[i] == 'A' or frase[i] == 'E' or frase[i] =='I' or frase[i] =='O' or frase[i] =='U':
            i+=1
            
        else:
            str.upper(frase[i])
            i+=1
            
            
        return frase