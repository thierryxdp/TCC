def conta_frases(frase):
    x = frase.count(".")+frase.count("...")+frase.count("!")+frase.count("?")
    return len(x)