def conta_frases(frase):
    """..."""
    x = frase
    y = "."
    return str.count(x, y) + str.count(x, "!") + str.count(x, "?") + str.count(x, "...")