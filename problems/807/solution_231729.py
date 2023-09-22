def conta_frases (texto):
    """Conta o número de frases na entrada. Cada frase do texto termina rm ".", "!", "?" ou "...". str -> int"""
    frases = (str.count(texto, '?')) + (str.count(texto, '!')) + (((str.count(texto, '.'))-(str.count(texto, '...')))*3)
    return frases