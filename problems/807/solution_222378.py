def conta_frases (texto):
    """ conta as frases do texto colocado em string
    str -> int"""
    str.count (texto, '.') + str.count (texto, '!') + str.count (texto, '?') + str.count (texto, '...')