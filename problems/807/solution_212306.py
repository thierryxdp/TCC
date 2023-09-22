def conta_frases(frases):
    """retorna o numero de frases"""
    frases = str.replace(frases, '!', '.')
    frases = str.replace(frases, '?', '.')
    frases = str.replace(frases, '...', '.')
    return len(str.split(frases, '.'))-1