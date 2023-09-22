def conta_frases (texto):
    """Retorna o número de frases que aparecem num determinado texto.
    Entrada: str
    Saída: int
    """
    return str.count(texto, "?") + str.count(texto, "!") + str.count(texto, ".") - str.count(texto, "...")*2