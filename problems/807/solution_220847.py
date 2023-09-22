def conta_frases(frases):
    """..."""
    x = frase.count("." and not "...")
    y = frase.count("...")
    a = frase.count("?")
    b = frase.count("!")
    return x + y + a + b