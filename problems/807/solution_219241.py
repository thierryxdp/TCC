def conta_frases(frases):
    """Conta quantas frases tem na string de entrada;
    str -> int"""
    n_frases= frases.count("!") + frases.count("?") + frases.count("...") + frases.count(".") - 3 * frases.count("...")
    return n_frases