def conta_frases(texto):
    """conta o número de frases que aparecem no texto;
    string -> tupla"""
    x = texto.count("...")
    x = texto.count(".")
    y = texto.count("!")
    w = texto.count("?")
    h = texto.count("...")*3
    return (x+y+w+z)-h