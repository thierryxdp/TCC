def conta_frases(texto):
    '''.'''
    
    if '...' in texto:
        return texto.count(str.replace(texto,'...','.')) + 1 
    else:
        return  str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')