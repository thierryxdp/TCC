def conta_frases(texto):
    """..."""
        
    if '...' in texto: 
        return str.replace(str.count(texto,'...')) +  str.count(texto,'?') + str.count(texto,'!')
  
    else:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')