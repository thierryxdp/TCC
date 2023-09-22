def conta_frases(frases):
    num_frases= ((str.count(frases, '...') + str.count(frases, '.'))//2) + str.count(frases,'!') + str.count(frases,'?') + str.count(frases, '.')
    return num_frases