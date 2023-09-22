def conta_frases(texto):
    
    
    frase=[str.count(str.split(texto,'.')+
           str.split(texto,'?')+
           str.split(texto,'!')+
           str.split(texto,'...'))]
    
            
    return len(frase)