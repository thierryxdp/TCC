def conta_frases(texto):
    ''' '''
    a=str.count(texto,'.')
    b=str.count(texto,'...')
    return a+b+2