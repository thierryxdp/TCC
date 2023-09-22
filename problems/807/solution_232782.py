def conta_frases(x):
    '''função que conta frases no texto x'''
    return str.count(x,'.') - (3*str.count(x,'...') + str.count(x,'!') + str.count(x,'?')