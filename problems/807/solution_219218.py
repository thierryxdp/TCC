def conta_frases(texto):
    x = str.count(texto, ".")
    y = str.count(texto, "!")
    z = str.count(texto, "?")
    j = str.count(texto, "...") - (x-1)
    i = str.count(texto, ";")
    return x + y + z + j  + i