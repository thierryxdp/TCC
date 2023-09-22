def conta_frases(texto):
    sempontos = ''
    for c in texto:
        if c.ispunctuation:
            sempontos += c
    return sempontos