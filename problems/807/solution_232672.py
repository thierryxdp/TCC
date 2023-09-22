conta_frases(texto):
    """Conta o número de frases que aparecem no texto. string -> int"""
    return len(texto.split("!" or "." or "?" or "..."))