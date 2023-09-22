def conta_frases(frases):
    frases = frases.replace("...","@")
    frases = frases.replace(".", "@")
    frases = frases.replace("!", "@")
    frases = frases.replace("?", "@")
    frases = frases.split("@")
    frases = len(frases) - 1
    return frases