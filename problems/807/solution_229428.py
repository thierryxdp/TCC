def conta_frases(texto):
    '''função que conta quantas frases há no texto'''
    'str->int'
    if '?' is in (texto):
    return str.count('texto','?')
    
    if '.' is in (texto):
    return str.count('texto','.')

    if '...'is in (texto):
    return str.count('texto','...')

    elif '!' is in (texto):
    return str.count('texto','!')