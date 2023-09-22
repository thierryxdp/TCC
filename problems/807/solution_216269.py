def conta_frases(frase):
    x = frase.split(".")+("...")+("!")+("?")
    return len(x)