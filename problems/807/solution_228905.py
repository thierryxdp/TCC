def conta_frases(texto):
    ''' Docs
    str -> int '''

    a = texto

    total1 = str.count(a, '.', '!')
    total2 = str.count(a, , '?', '...')

    return total1 + total2