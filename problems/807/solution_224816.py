def conta_frases(frases):
    reticencias == '...'
    ponto == '.'
    num_frases= str.count(frases, reticencias) + str.count(frases,'!') + str.count(frases,'?') + str.count(frases, ponto)
    return num_frases