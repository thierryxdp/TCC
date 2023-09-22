def conta_frases(frases):
    num_frases= str.count(frases, reticencias) + str.count(frases,'!') + str.count(frases,'?') + str.count(frases, ponto)
    reticencias == '...'
    ponto == '.'
    return num_frases