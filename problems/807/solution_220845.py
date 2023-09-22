def conta_frases(frases):
    """..."""
    frase = frases.split()
	x = frase.count(".")
    y = frase.count("...")
    a = frase.count("?")
    b = frase.count("!")
    return x + y + a + b