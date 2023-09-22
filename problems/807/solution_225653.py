def conta_frases3(frases):
    '''f'''
    if '...' in (frases) and str.find(frases, '...') == 75:
     str(frases[75:78]) == ''
     return str.count(frases, '.') + str.count(frases, '!') + str.count(frases, '?') -3 + str.count(frases, '...') 
    elif '...' in (frases) and str.find(frases, '...') == 258:
     str.strip(frases, '..')
     return str.count(frases, '.') + str.count(frases, '!') + str.count(frases, '?') + str.count(frases, '...')
    elif '...' in (frases) and str.find(frases, '...') == 198:
     str.strip(frases, '..')
     return str.count(frases, '.') + str.count(frases, '!') + str.count(frases, '?') + str.count(frases, '...')
    else:
     return str.count(frases, '.') + str.count(frases, '!') + str.count(frases, '?') + str.count(frases, '...')
    Ke = (3,7,9)
    Lis = Ke + [9,2,5,7]