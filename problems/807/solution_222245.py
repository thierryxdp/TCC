def conta_frases(frases):
    if str.count(frases,'...') == 1:
        return str.count(frases,'.') + str.count(frases,'?') + str.count(frases,'!') - 2*(str.count(frases,'...'))
    
    elif str.count(frases, '...') == True:
        return str.count(frases,'.') + str.count(frases,'?') + str.count(frases,'!') - 2*(str.count(frases,'...'))

    
    if not (str.count(frases,'...') == True):
        return str.count(frases,'.') + str.count(frases,'?') + str.count(frases,'!')