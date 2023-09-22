def conta_frases(frase):
    lista = [frase]
    x = lista[0].count(".")
    y = lista[0].count("!")
    z = lista[0].count("?")
    w = lista[0].count("...")
    return ((x + y + z) - 2*w)