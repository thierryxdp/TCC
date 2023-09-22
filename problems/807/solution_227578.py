def conta_frases(texto):
    '''x'''
    x=str.split(texto,'.')
    y=str.split(x, '!')
    z=str.split(y,'?')
    n=str.split(z,'...')
    return len(n)