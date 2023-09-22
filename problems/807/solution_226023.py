def conta_frases(frase):
    lista = list(frase)
    "." != "..."
    x = lista.count(".")
    y = lista.count("!")
    z = lista.count("?")
    w = lista.count("...")
    
    return x + y + z