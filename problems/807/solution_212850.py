def conta_frases(frases):
    if str.count(frases, '.')>0:
        return (str.count(frases, '.') - (str.count(frases, '...')%3 + str.count(frases, '...')) + str.count(frases,'!') + str.count(frases, '?') 
    
    if str.count(frases, '.') == 0:
        return str.count(frases,'?') + str.count(frases, '...') + str.count(frases,'!')