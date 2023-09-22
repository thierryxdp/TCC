def conta_frases(frase):
    """ essa função tem como caracteristica contar quantas frases existem por seu final, sendo ponto de exclamação, interrogação, reticências ou ponto final
    entrada -> str
    saida -> int """
    i = str.count(frase, "?")
    e = str.count(frase, "!")
    p = str.count(frase, ".")
    r = str.count(frase, "...")
    conta = i + e + p + r
    if r > 0:
        conta = conta  - (r*3)
    return conta