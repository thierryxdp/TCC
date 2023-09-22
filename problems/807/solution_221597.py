def conta_frases(texto):
    """Recebe um texto e retorna o número de frases que aparecem;
    str -> int"""
    texto_separado = texto.split(".", "!", "?", "...")
    return len(texto_separado)