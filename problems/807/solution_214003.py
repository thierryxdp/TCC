def conta_frases(frase):
    """ """
    frase=  frase.replace("...", ".").replace("!",".").replace("?",".")
    a=frase.split(".")
    return len(a)-1