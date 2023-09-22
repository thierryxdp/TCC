def conta_frases(s):
    '''...'''
    w=s.count('!')
    x=s.count('?')
    y=s.count('...')
    z=s.count('.')
    return w+x+(y-2)+z