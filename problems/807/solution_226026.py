def conta_frases(frase):
    x = frase.split(".")
    y = frase.split("; ")
    z = frase.split("!")
    w = frase.split("?")
    k = frase.split("...")
    return len(x) + len(y) + len(z) + len(w) + len(k)