def conta_frases(frases):
    """..."""
    x = frases.count(".")
    y = frases.count("...")
    a = frases.count("?")
    b = frases.count("!")
    return x + y + a + b