def conta_frases(texto):
    sempontos = ''
    for c in texto:
        if c == '.,!?':
            sempontos += c
    return len(sempontos)