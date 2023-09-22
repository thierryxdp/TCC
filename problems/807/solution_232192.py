def conta_frases (frase):
    """Conta o número de frases que há num texto, str->int"""
    frase = tuple(frase)
    x = tuple.count ('?',frase[0:])
    y = tuple.count ('!',frase[0:])
    z = tuple.count ('.',frase[0:])
    return x + y + z