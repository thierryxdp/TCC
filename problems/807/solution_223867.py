def conta_frases(texto):
    '''.'''
    '...' = '...'+'...' = 2
    if '...' in texto:
        return  (str.count(texto, '...') + str.count(texto, '?') + str.count(texto, '!') + str.count(texto, '.'))
  
    else:
        return  str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')