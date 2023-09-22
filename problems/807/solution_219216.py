def conta_frases(texto):
    x = str.count(texto, ".")
    y = str.count(texto, "!")
    z = str.count(texto, "?")
    j = str.count(texto, "...") - (x-1)
    return x + y + z + j