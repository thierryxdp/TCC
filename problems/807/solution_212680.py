def conta_frases(texto):
    """ função que conta o número de frases que aparecem no texto, podendo ser separadas por ponto final, de exclamação, interrogação ou reticencias"""
    return str.count(texto,".")+ str.count(texto,"!")str.count(texto,"?") - 2*str.count(texto,"...")