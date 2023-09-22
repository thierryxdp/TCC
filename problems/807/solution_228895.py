def conta_frases(frase):
    frase.partition('.').partition('?').partition('!').partition('...')
    return len(frase)