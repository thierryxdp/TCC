def conta_frases(texto):
    texto=texto.replace("...",".")
    texto=list(texto)
    a=texto.count("!")
    b=texto.count("?")
    c=texto.count(".")
    return a+b+c