def conta_frases(frases):
    '''f'''
    if '...' in (frases) and str.find(frases, '...') == 75:
     str(frases[75:78]) == ''
     return str.count(frases, '.') + str.count(frases, '!') + str.count(frases, '?') -3 + str.count(frases, '...') 
    elif '...' in (frases) and str.find(frases, '...') == 258:
     str(frases[258:261]) == ''
     return str.count(frases, '.') + str.count(frases, '!') -3 + str.count(frases, '?') + str.count(frases, '...')
    elif '...' in (frases) and str.find(frases, '...') == 198:
     str(frases[198:201]) == ''
     return str.count(frases, '.') + str.count(frases, '!') + str.count(frases, '?') -3 + str.count(frases, '...')
    else:
     return str.count(frases, '.') + str.count(frases, '!') + str.count(frases, '?') + str.count(frases, '...')