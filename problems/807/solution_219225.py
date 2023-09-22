def conta_frases(texto):
    x = str.count(texto, ".")
    y = str.count(texto, "!")
    z = str.count(texto, "?")
    j = str.count(texto, "...") 
    if j > 0:
        x = x - 3*j
        return x + y + z + j
    else:
        return x + y + z + j