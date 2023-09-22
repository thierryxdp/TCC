def conta_frases (frase):
    """Conta o número de frases que há num texto, str->int"""
    frase = list(frase)
    x = str.count ('?',frase[0:])
    y = str.count ('!',frase[0:])
    z = str.count ('.',frase[0:])
    return x + y + z