def conta_frases(frase):
    x = frase.count(".")
    y = frase.count("...")
    a = frase.count("?")
    b = frase.count("!")
    x = x-3*y
    return x + y + a + b