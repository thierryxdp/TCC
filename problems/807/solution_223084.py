def conta_frases(texto):
    texto=texto.replace("!",".")
    texto=texto.replace("?",".")
    texto=texto.replace("...",".")
    texto=texto.split(".")
    return texto