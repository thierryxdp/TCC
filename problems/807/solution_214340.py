def conta_frases(frase):
    """ essa função tem como caracteristica contar quantas frases existem por seu final, sendo ponto de exclamação, interrogação, reticências ou ponto final
    entrada -> str
    saida -> int """
    interrogação = str.count(frase, "?")
    exclamação = str.count(frase, "!")
    ponto_final = str.count(frase, ".")
    reticencias = str.count(frase, "...")
    conta = interrogação + exclamação + ponto_final + reticencias
    if reticencias > 0:
        conta = conta -3
    return conta