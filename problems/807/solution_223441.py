def conta_frases(texto):
    """..."""
    if '...' in texto: 
        return texto.count(texto.replace('...','.'))
  
    else:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')