def conta_frases(texto):
    sempontos = ''
    for c in texto:
        if c == '.' or c== ',' or c=='!' or '?':
            sempontos += c
    return sempontos.count()