def conta_frases(frases):
    '''f'''
    return str.count(frases, '. ') + str.count(frases, '!') + str.count(frases, '?') + str.count(frases, '...')