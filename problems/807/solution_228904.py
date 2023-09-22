def conta_frases(texto):
    ''' Docs
    str -> int '''

    a = texto

    total = str.count(a, '.', '!', '?', '...')

    return total