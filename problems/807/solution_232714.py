def conta_frases (texto):
    str.count(texto, ".")
    str.count(texto,"!")
    str.count(texto, "?")
    return str.count(texto, ".") + str.count(texto,"!") + str.count(texto, "?") + str.count(texto, "."*3)