def conta_frases (frase):
    """Conta o número de frases que há num texto, str->int"""
    a = list(frase)
    x = list.count ('?',a[0:])
    y = list.count ('!',a[0:])
    z = list.count ('.',a[0:])
    return list.count ('.',a[0:])