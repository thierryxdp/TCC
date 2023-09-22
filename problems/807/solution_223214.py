def conta_frases(frase):
    """..."""
    x = frase
    return str.count(x, ".") + str.count(x, "!") + str.count(x, "?") + str.count(x, "...")