def conta_frases(texto):
    '''.'''
    
    if '...' in texto:
        str.replace(texto,'...','.')
        return str.count(texto, '...') + str.count(texto, '?') + str.count(texto, '!') + str.count(texto, '.')
  
    else:
        return  str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')