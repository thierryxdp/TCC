def conta_frases(texto):
    """ função que conta o número de frases que aparecem no texto, podendo ser separadas por ponto final, de exclamação, interrogação ou reticencias"""
    x= "!" or "?"
    y= "."
    return str.count(texto,x) + str.count(texto,y) - 2*y