def conta_frases (texto):
    """ conta a quantidade de frases no texto acima
    str -> int"""
    a = str.count(texto,".")
    b = str.count(texto, "!")
    c = str.count(texto,"?")
    d = str.count(texto,"...")
    return a+b+c+d