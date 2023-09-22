def conta_frases(texto):
    return str.count(texto, '. ' or '! ' or '? ' or '... ', 0, len(frases))