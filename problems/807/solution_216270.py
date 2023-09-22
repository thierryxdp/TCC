def conta_frases(frase):
    x = frase.split(".")+frase.split("...")+frase.split("!")+frase.split("?")
    return len(x)