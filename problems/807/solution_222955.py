def conta_frases (texto):
    """Retorna o número de frases que aparecem num determinado texto.
    Entrada: str
    Saída: int
    """
    F = str.strip(texto, "?")
    F = str.strip(F, "!")
    return len(F)