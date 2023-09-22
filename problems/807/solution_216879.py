def conta_frases(texto):
    """conta o número de frases que aparecem no texto;
    string -> tupla"""
    contar = texto.count(".")
    y = texto.count("!")
    return contar+y