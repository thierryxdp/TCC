def conta_frases(texto):
    texto1 = str.count(texto, ".")
    texto2 = str.count(texto, "...")
    texto3 = str.count(texto, "!")
    texto4 = str.count(texto, "?")
    return len(texto1) + len(texto2) + len(texto3) + len(texto4)