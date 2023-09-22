def conta_frases(texto):
    """conta o numero de frases que aparecem em um dado
    texto (determinadas por . ou ! ou ? ou ...)
    str -> int"""
    x = int(str.count(texto,"...")) + int(str.count(texto,".."))
    x+=int(str.count(texto,"?"))+ int(str.count(texto,"!"))
     return x