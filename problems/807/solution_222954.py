def conta_frases (texto):
    """Retorna o número de frases que aparecem num determinado texto.
    Entrada: str
    Saída: int
    """
    F = str.strip(texto, "?")
    return len(F)