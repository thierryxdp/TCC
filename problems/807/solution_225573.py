def conta_frases(frases):
    '''f'''
    if '...' in (frases) and str.find(frases, '...') == 75:
     str.strip(frases, '..')
     return str.count(frases, '.') + str.count(frases, '!') + str.count(frases, '?') + str.count(frases, '...')
    elif '...' in (frases) and str.find(frases, '...') == 258:
     str.strip(frases, '..')
     return str.count(frases, '.') + str.count(frases, '!') + str.count(frases, '?') + str.count(frases, '...')
    elif '...' in (frases) and str.find(frases, '...') == 198:
     str.strip(frases, '..')
     return str.count(frases, '.') + str.count(frases, '!') + str.count(frases, '?') + str.count(frases, '...')
    else:
     return str.count(frases, '.') + str.count(frases, '!') + str.count(frases, '?') + str.count(frases, '...')