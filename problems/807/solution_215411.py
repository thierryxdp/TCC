def conta_frases(texto):
    """ """
    texto = texto.replace("...",".")
    return (str.count(texto,"!") + str.count(texto,"?") + str.count(texto,"."))