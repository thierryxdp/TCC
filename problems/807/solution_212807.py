def conta_frases(frases):
    if str.count(frases, '.')>0:
        return str.count(frases, '.') + str.count(frases, '!')
    
    if str.count(frases, '?')>0:
        return str.count(frases, '?')
    
    if str.count(frases, '.')>0 and str.count(frases, '?')>0:
        return str.count(frases, '.' and '?')