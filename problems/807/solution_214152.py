def conta_frases(texto):
    texto.split(".")
    texto.split("!")
    texto.split("...")
    texto.split("?")
    return len(texto.split("."))+len(texto.split("!"))+len(texto.split("..."))+len(texto.split("?"))