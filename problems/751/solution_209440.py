def quant_palavras(frase):
    lista = list(frase)
    x = lista.count(".")
    y = lista.count("!")
    z = lista.count("?")
    w = lista.count(",")
    w2 = lista.count(", ")
    w3 = lista.count(" ,")
    m = lista.count(";")
    m1 = lista.count("; ")
    m2 = lista.count(" ;")
    return x + y + z + w + m + w1 + w2 + m1 + m2