def conta_frases(texto):
    texto.split(" ")
    texto.count(".")
    texto.count("!")
    texto.count("...")
    texto.count("?")
    return len(texto.count("."))+len(texto.count("!"))+len(texto.count("..."))+len(texto.count("?"))