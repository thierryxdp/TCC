def conta_frases(texto):
    '''.'''
    
    if '...' in texto:
        return texto.split(str.replace('...','.'))
    else:
        return  str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')