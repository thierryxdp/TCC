def conta_frases(frase):
    lista = [frase]
    x = lista[0].count(".")
    x1 = lista[0].count(". ")
    y = lista[0].count("! ")
    y1 = lista[0].count("!")
    z = lista[0].count("? ")
    z1 = lista[0].count("?")
    w = lista[0].count("... ")
    w1 = lista[0].count("...")
    
    
    return x + x1 + y + y1 + z + z1 + w1