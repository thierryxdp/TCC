def conta_frases(texto):
    ''' função  que conta o número de frases que
    aparecem num texto.
    str>>int'''
    a=str.count(texto,'!')+str.count(texto,'?')
    b=str.count(texto,'.')
    c=str.count(texto,'...')
    d=c-(3*b)
    return a+b+d