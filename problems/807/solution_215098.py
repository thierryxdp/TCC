def conta_frases(texto):
    a = texto.split("!")
    b = texto.split("?")
    c = texto.split(".")
    d = texto.split("...")
    return len(a)+len(b)+len(c)+len(d)