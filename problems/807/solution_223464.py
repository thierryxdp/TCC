def conta_frases(texto):
    """..."""
    
    if '...' in texto: 
        texto.replace('...','.')
        return texto.split('.') +  str.count(texto,'?') + str.count(texto,'!')
  
    else:
        return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')