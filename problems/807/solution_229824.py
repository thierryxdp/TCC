def conta_frases(texto):
    ''' função  que conta o número de frases que
    aparecem num texto.
    str>>int'''
    return str.count(texto,'.')+str.count(texto,'!')+str.count(texto,'?')