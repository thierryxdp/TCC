def conta_frases(frases):
    """Calcula e retorna a o número de frases que tem na
variável de entrada frases; str --> int"""
    y= frases.split("!" or "..." or "."or"?")
    return len(y)