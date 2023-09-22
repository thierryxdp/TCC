def conta_frases(texto):
    """Função que conta o número de frases em um texto;
    str -> int"""
    return len(str.split(texto,"!.?..."))