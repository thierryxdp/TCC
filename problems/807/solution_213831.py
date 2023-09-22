def conta_frases (frase):
    x = str.split(frase)
    y = frase.rsplit("!", maxsplit=2)
    return y