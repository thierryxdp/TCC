def conta_frases(texto):
    """conta o número de frases que aparecem no texto;
    string -> tupla"""
    x = texto.count(".")
    y = texto.count("!")
    w = texto.count("?")
    reticencia = ...
    z = texto.count("reticencia")
    return x+y+w+z