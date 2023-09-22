def conta_frases(frase):
    variavel = "."
    y = frase.count(".")
    x = frase.count("...")
    a = frase.count("?")
    b = frase.count("!")
    return x + y + a + b