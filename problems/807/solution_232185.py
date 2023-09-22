def conta_frases (frase):
    """Conta o número de frases que há num texto, str->int"""
    frase = list(frase)
    x = list.count ('?',frase[0:])
    y = list.count ('!',frase[0:])
    z = list.count ('.',frase[0:])
    return x + y + z