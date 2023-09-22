def conta_frases(frase):
    """..."""
    x = frase
    y = "..."
    return str.count(x, ".") + str.count(x, "!") + str.count(x, "?") + str.count(x, y)