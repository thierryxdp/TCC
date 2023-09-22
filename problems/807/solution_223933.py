def conta_frases(texto):
    '''Retorna a quantidade de frases no texto dado como entrada da função.
str --> int
'''
    mod = str.replace(texto,'...','.')
    return str.count(mod,'.')+ str.count(mod,'?')+ str.count(mod,'!')