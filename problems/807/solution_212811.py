def conta_frases(frases):
        return str.count(frases, '.') + str.count(frases, '!') +  return str.count(frases, '?')
    
    if str.count(frases, '?')>0:
        return str.count(frases, '?')