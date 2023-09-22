def conta_frases(texto):
    """Dado um texto retorna a quantidade de frases nele.
    str -> int """
    pontos = texto.count(".")+texto.count("!")+texto.count("?")+texto.count("...")
    return pontos