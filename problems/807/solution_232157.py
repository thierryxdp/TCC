def conta_frases (frase):
    """Conta o número de frases que há num texto, str->int"""
    frase = str.split (frase)
    return len (list.count ('.',frase[0:])) + len (list.count ('!',frase[0:])) + len (list.count ('?',frase[0:]))