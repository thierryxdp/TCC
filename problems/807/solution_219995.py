def conta_frases (texto):
    str(frases1) = texto.split(".")
    str(frases2) = frases1.split("!")
    str(frases3) = frases2.split("?")
    frases4 = frases3.split("...")
    numero_frases = len(frases4)
    return numero_frases