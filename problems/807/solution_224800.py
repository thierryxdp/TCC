def conta_frases(frases):
    num_frases= str.count(frases,'...') + str.count(frases,'!') + str.count(frases,'?') + str.count(frases, '.')
    return num_frases