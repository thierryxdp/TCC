def conta_frases (f):
    '''...'''
    if '.' != '...':
        return f.count('.') and ('...')
    return f.count('.') + f.count('!') + f.count('?') + f.count('...')