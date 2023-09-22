def conta_frases(texto):
    """conta a quantidade de frases em um texto"""
    a = texto.split(".")
    b = texto.split("...")
    c = texto.split("!")
    d = texto.split("?")
    return len(a,b,c,d)