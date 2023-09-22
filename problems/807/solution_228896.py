def conta_frases(frase):
    novo = frase.partition('.').partition('?').partition('!').partition('...')
    return len(novo)