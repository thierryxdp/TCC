def conta_frases(texto):
    
    
    frase=[str.split(texto,'.')+
           str.split(texto,'?')+
           str.split(texto,'!')+
           str.split(texto,'...')]
    
            
    return len(frase+texto)