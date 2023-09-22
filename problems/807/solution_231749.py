def conta_frases(frase):
    y=str.replace(frase, "...", ".")
    y=str.replace(y, "?", ".")
    y=str.replace(y, "!", ".")
    y=str.split(y, ".")
    return len(y) - 1