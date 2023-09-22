def quant_palavras(frase):
    lista = list(frase)
    x = lista.count(".")
    y = lista.count("!")
    z = lista.count("?")
    w = lista.count(",")
    m = lista.count(";")
    return x + y + z + w + m