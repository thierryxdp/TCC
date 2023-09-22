def conta_frases(frases):
    str.count(frases, '...') == 1
    num_frases= str.count(frases, '...') + str.count(frases, '.') + str.count(frases, '!') + str.count(frases, '?')
    return num_frases