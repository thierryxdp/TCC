def conta_frases(texto):
    """..."""
    texto.replace('...','.')
    
    if '...' in texto: 
        return texto.strip('.')
  
    else:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')