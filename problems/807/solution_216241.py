def conta_frases(frase):
    f = frase.split(".")+frase.split("...")+frase.split("!")+frase.split("?")
    return len(f)