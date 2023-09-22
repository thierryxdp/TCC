def conta_frases(frase):
    interro = frase.count("?")
    exclam = frase.count("!")
    trespont = frase.count("...")
    ponto = frase.count(". ")
    
    return interro + exclam + trespont + ponto