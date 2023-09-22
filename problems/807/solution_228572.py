def conta_frases(texto):
    
    
    frase1=[str.split(texto,'.')]+[str.split(texto,'?')]+[str.split(texto,'!')]+[str.split(texto,'...')]
    
            
    
     return len(frase1)