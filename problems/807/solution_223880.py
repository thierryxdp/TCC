def conta_frases(texto):
    '''.'''
    lista = str.replace(texto, '...','.')
    if '...' in texto:
        return  str.count(lista,'.') + str.count(texto, '?') + str.count(texto, '!') + str.count(texto, '.') - int(3)
  
    else:
        return  str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')