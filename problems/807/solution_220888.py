def conta_frases(frase):
    x = frase.count("." != "...")
    y = frase.count("...")
    a = frase.count("?")
    b = frase.count("!")
    return x + y + a + b