def conta_frases(texto):
    '''.'''
    lista = str.replace(texto, '...','.')
    if '...' in texto:
        return texto.split(str.replace(lista,'...','.'))
    else:
        return  str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'.')