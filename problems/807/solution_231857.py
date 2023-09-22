def conta_frases(frase):
    x = str.replace(frase, "...", ".")
    x = str.replace(x, "?", ".")
    x = str.replace(x, "!", ".")
    x = str.split(x, ".")
    return len(x) - 1