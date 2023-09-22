def conta_frases (f):
    '''...'''
    if '.' != '...':
        return f.count('.') or f.count('...')
    return f.count('.') + f.count('!') + f.count('?') + f.count('...')