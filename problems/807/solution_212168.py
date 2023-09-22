def conta_frases(texto):
    ''' '''
    return str.count(texto,'!')+ str.count(texto,'?')+((str.count(texto,'.')+str.count(texto,'...'))-3*str.count(texto,'...'))