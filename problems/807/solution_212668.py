def conta_frases(texto):
    """ função que conta o número de frases que aparecem no texto, podendo ser separadas por ponto final, de exclamação, interrogação ou reticencias"""
    x= "!" or "?" or "."
    return str.count(texto,x) -2*(".")