def conta_frases(frase):
    """ essa função tem como caracteristica contar quantas frases existem por seu final, sendo ponto de exclamação, interrogação, reticências ou ponto final
    entrada -> str
    saida -> int """
    interrogaçao = str.count(frase, "?")
    exclamaçao = str.count(frase, "!")
    pontofinal = str.count(frase, ".")
    reticencias = str.count(frase, "...")
    conta = interrogação + exclamação + pontofinal + reticencias
    if reticencias > 0:
        conta = conta  - (reticencias*3)
    return conta