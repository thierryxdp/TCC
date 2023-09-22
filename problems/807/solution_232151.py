def conta_frases (frase):
    """Conta o número de frases que há num texto, str->int"""
    frase = str.split (frase)
    return list.count ('.',frase[0:]) + list.count ('!',frase[0:]) + list.count ('?',frase[0:])