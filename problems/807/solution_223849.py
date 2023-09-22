def conta_frases(frase):
    '''.'''
    
    if '...' in texto: 
        return str.count(texto, '...') + str.count(texto, '?') + str.count(texto, '!') + str.count(texto, '.')
  
    else:
        return  str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')