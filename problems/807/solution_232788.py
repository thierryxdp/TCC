def conta_frases(texto):
    '''função que conta frases no texto x'''
    return (str.count(texto,'.') - (3*str.count(texto,'...') + str.count(texto,'!') + str.count(texto,'?'))