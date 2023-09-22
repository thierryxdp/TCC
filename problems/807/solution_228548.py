def conta_frases(texto):
    
    
    morcego=[str.split(texto,'.') and
           str.split(texto,'?')and
           str.split(texto,'!')and
           str.split(texto,'...')]
            
    
    return len(morcego)