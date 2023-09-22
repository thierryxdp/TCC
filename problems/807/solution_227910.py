def conta_frases(texto):
    frases = str.replace(texto, '!', '.')
    frases = str.replace(frases, '?', '.')
    frases = str.replace(frases, '...', '.')
    quatidade_frases = str.split(frases,'.')
    return len(quantidade_frases)