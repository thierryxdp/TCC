def conta_frases(texto):
    """conta o número de frases que aparecem no texto;
    string -> tupla"""
    x = texto.count(".")
    y = texto.count("!")
    w = texto.count("?")
    z = texto.count("...")
    z = z//3
    return x+y+w+max(z)