def conta_frases (frase):
    """Conta o número de frases que há num texto, str->int"""
    return str.count ('.',frase[0:]) + str.count ('!',frase[0:]) + str.count ('?',frase[0:]) - 2 * str.count ('...',frase[0:])