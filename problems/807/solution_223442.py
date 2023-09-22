def conta_frases(texto):
    """..."""
    if '...' in texto: 
        return texto.replace('...','.')
  
    else:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')