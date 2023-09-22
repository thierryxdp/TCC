def conta_frases(texto):
    """ conta quantias frases tem no texto dado."""
    texto = str.partition(texto, '!') + str.partition(texto, '.') + str.partition(texto, '...') +     str.partition(texto, '?')