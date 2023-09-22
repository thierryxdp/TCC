def conta_frases(texto):
    '''x'''
    x=str.split(texto,'.')
    y=list.remove(x, '!')
    z=list.remove(y,'?')
    n=list.remove(z,'...')
    return len(n)