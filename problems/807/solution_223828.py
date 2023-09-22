def conta_frases(texto):
    '''.'''
    
    if '...' in texto:
        return texto.count(str.replace(texto,'...','.')) + len 
    else:
        return  str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')