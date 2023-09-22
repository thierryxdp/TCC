def conta_frases(s):
    '''...'''
    w=s.count('!')
    x=s.count('?')
    y=s.count('...')-2
    z=s.count('.')
    return w+x+y+z