def conta_frases(texto):
    '''.'''
    
    if '...' in texto:
        return
    else:
        return  str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')