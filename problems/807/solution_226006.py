def conta_frases(texto):
    texto1 = str.count(texto, ".")
    texto2 = str.count(texto, "...")
    texto3 = str.count(texto, "!")
    texto4 = str.count(texto, "?")
    return int(texto1 + texto2 + texto3 + texto4)