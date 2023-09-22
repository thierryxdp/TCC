def conta_frases(texto):
    return str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'...') + len(str.split(texto,'. ')) - 1