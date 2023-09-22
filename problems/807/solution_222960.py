def conta_frases (texto):
    """Retorna o número de frases que aparecem num determinado texto.
    Entrada: str
    Saída: int
    """
    F = str.split(texto, "?")
    G = str.split(F, "!")
    return len(G)