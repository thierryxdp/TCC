def uppCons(frase):
    
    i=0
    novafrase=[]
    
    frase=str.upper(frase)
    
    while i<len(frase):
        if frase[i]!='A' or 'E' or 'I' or 'O' or 'U':
            novafrase.append(frase[i])
            i+=1
            
        else:
            i+=1
            
            novafrase=str(novafrase)
        return novafrase