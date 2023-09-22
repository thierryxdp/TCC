def conta_frases(frase):
    ponto = frase.count(".")
    excla = frase.count("!")
    inter = frase.count("?")
    reti = frase.count("...")
    return ponto + excla + inter + reti