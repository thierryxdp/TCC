def conta_frases(texto):
    """Retorna o número de frases em um texto
    assinatura: str -> int"""
    separador = '.', '!', '?', '...'
    return len(str.split(texto, separador))