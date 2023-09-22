def conta_frases(texto):
    '''função que conta o numero de frases que aparecem num texto, com suas pontuações;
    str-> int'''
    w=str.count(texto,'!')+str.count(texto,'?')
    x=str.count(texto,'...')
    y=str.count(texto,'.')
    return w+x+y