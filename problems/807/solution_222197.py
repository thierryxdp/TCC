def conta_frases(frases):
    return str.count(frases,'...') + (str.count(frases,'.'))/3 + str.count(frases,'?') + str.count(frases,'!')