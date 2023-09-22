def conta_frases(frase):
    lista = [frase]
    x = lista.count(". ")
    x1 = lista.count(".")
    y = lista.count("! ")
    y1 = lista.count("!")
    z = lista.count("? ")
    z1 = lista.count("?")
    w = lista.count("... ")
    k = lista.count("; ")
    
    
    return x + x1 + y + y1 + z + z1 + k