def conta_frases(texto):
    '''.'''
   
    if '...' in texto:
        return  str.count(texto, '...') + str.count(texto, '?') + str.count(texto, '!') + str.count(texto, '.') - int(3)
    if ('...')*2 in texto:
        return  str.count(texto, '...') + str.count(texto, '?') + str.count(texto, '!') + str.count(texto, '.') - int(6)
  
    else:
        return  str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')