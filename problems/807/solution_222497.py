def conta_frases (texto):
    """ conta a quantidade de frases no texto acima
    str -> int"""
    a = str.count(texto,".")
    b = str.count(texto, "!")
    c = str.count(texto,"?")
    d = str.count(texto,"...")
    if d != 0:
        return a+b+c+d - a*3
    else:
    return a+b+c+d