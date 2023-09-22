def conta_frases(texto):
    '''.'''
    
    if '...' in texto:
        return texto.count(texto.replace('...','.'))
    if '...'<2:
        return 4
    else:
        return  str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')