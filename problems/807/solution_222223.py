def conta_frases(frases):
    if str.count(frases,'...') == True:
        return str.count(frases,'.') + str.count(frases,'?') + str.count(frases,'!') - 2