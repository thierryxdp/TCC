def conta_frases(frases):
    """Funçao que conta o numero de frases que aparecem no texto.
    As frases podem ser terminadas com ponto final, exclamaçao, interrogaçao ou reticencias"""
    a = str.count(texto,"...")
    b = str.count(texto,"!")
    c = str.count(texto,"?")
    d = str.count(texto,".")
    n = a+b+c+d
    if a>0:
        return n-3*a
    else:
        return n