def conta_frases(frase):
    x = frase.split(".")+frase.count("...")+frase.count("!")+frase.count("?")
    return len(x)