def conta_frases(texto):
    
    
    morcego=[str.split(texto,'.')+
           str.split(texto,'?')+
           str.split(texto,'!')+
           str.split(texto,'...')]
            
    
    return morcego