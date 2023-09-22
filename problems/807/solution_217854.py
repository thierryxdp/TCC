def conta_frases(x):
    '''Conta o número de frases dadas de entradas.
    str -> int'''
    s=str.partition(x,'!') and str.partition(x,'?') and str.partition(x,'...') and str.partition(x,'.')
    return len(s)