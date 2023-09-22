def quant_palavras(frase):
    lista = list(frase)
    x = lista.count(".")
    y = lista.count("!")
    z = lista.count("?")
    return x + y + z