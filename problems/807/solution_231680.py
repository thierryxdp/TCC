def conta_frases(t):
    ''' retorna o número de frases que há em t;
    str -> int '''
    reticências = str.count(t,'...')
    ponto = (str.count(t,'.')-reticências)*3
    exclamação = str.count(t,'!')
    interrogação = str.count(t,'?')
    return reticências+ponto+exclamação+interrogação