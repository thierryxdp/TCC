def conta_frases(m):
    s=str.count(m,'.')
    a=str.count(m,'!')
    d=str.count(m,'?')
    f=str.count(m,'...')
    if '...' in m:
        g=str.count(m,'...')
        return a+s+d+f- (3*g)
    else:
        return a+s+d+f