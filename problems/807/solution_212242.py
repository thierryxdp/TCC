def conta_frases(frases):
    """retorna o numero de frases"""
    return str.count(str.replace(frases,'!','.','?'))