def conta_frases(frases):
    '''f'''
    if '...' in (frases):
    return str.count(frases, '.') + str.count(frases, '!') + str.count(frases, '?') + str.count(frases, '...')