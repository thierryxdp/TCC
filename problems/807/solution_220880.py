def conta_frases(frase):
    y = frase.count(".")
    x = frase.count("...")
    a = frase.count("?")
    b = frase.count("!")
    return x + y + a + b