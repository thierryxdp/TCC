def conta_frases(texto):
    """..."""
    
    if '...' in texto:
        texto.replace('...','.')
        
    if '...' in texto: 
        return str.count(texto,'...') +  str.count(texto,'?') + str.count(texto,'!')
  
    else:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')