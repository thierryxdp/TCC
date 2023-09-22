def conta_frases(t):
    ''' retorna o número de frases que há em t;
    str -> int '''
    reticencias = (str.count(t,'...'))
    ponto = (str.count(t,'.')- str.count(t,'...'))*3
    exclamacao = (str.count(t,'!'))
    interrogacao = (str.count(t,'?'))
    return reticencias+ponto+exclamacao+interrogacao