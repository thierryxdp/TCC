def conta_frases(frase):
    """..."""
    x = frase
    if "." in x:
    return str.count(x, ".") str.count(x, "!") + str.count(x, "?") + str.count(x, "...") - (3*str.count(x, "..."))