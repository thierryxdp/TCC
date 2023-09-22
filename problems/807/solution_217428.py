def conta_frases(frases):
    """Função que conta o número de frases inseridas, baseada nos pontos finais."""
    """Str -> Int"""
    return frases.count("...")-3*frases.count("...") + frases.count("!") + frases.count("?") + frases.count(".")