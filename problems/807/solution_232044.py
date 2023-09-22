def conta_frases(frases):
    """Calcula e retorna a o número de frases que tem na
variável de entrada frases; str --> int"""
    y= str.split(frases,"." or "!" or "...")
    return len(y)