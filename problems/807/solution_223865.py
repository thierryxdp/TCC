def conta_frases(texto):
    '''.'''
    
    if (('...')<(int(2))) in texto:
        return  (str.count(texto, '...') + str.count(texto, '?') + str.count(texto, '!') + str.count(texto, '.')) - int(3)
  
    else:
        return  str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')