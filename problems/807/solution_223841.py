def conta_frases(texto):
    '''.'''
    
    if '...' in texto:
        return texto.split(str.replace(texto,'...','.'))
    else:
        return  str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')