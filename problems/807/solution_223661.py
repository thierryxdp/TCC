def conta_frases(texto):
    '''Retorna a quantidade frases no texto dado como entrada na função.
'''
    mod = str.replace(texto,'...','.')
    return str.count(mod,'.')+ str.count(mod,'?')+ str.count(mod,'!')