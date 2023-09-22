def conta_frases(x):
    ''' retorna o número de frases que existe em x;
    str -> int '''
    reticencias = str.count(x,'...')
    ponto = str.count(x,'.')-(str.count(x,'...'))*3
    exclamacao = str.count(x,'!')
    interrogacao = str.count(x,'?')
    return reticencias+ponto+exclamacao+interrogacao