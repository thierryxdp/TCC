def posLetra(frase,letra,x):
    i=0
    b=0    
    while i<len(frase):
        if frase[i]==letra:
        	b=b+1            
        if b==x:
            break        
        i=i+1        
    if b<x:
        return -1
    return i