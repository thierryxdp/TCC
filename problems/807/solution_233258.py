def conta_frases(texto):
    sempontos = ''
    for c in texto:
        if c.punctuation:
            sempontos += c
    return sempontos