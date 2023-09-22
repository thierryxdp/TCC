def conta_frases(texto):
    """conta o número de frases que aparecem no texto;
    string -> tupla"""
    
    x = texto.split(".")
    y = texto.split("!")
    w = texto.split("?")
    z = texto.split("...")
    g = x,y,w,z
    t = len(g)
    return t