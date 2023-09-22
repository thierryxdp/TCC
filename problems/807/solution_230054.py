def conta_frases(frase):
    'conta o numero de frases str -> int'
    x = frase.replace("...",".")
    y = x.replace("?",".")
    z = y.replace("!",".")
    frases = z.split(".")
    return len(frases)-1