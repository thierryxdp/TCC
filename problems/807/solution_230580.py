def conta_frases(texto):
    trocado = str.replace(texto,'...', '.')
    return str.count(texto,'!') + str.count(texto,'?') + str.count(trocado, '.')