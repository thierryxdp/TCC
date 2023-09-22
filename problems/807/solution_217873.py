def conta_frases (texto):
    """Retorna e conta o número de frases que aparecem neste texto;
    str -> tupla"""
    pf = texto.count (".")
    e = texto.count ("!")
    i = texto.count ("?")
    p = texto.count ("...")
    return p+pf+e+i