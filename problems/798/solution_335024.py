def freq_palavras(frases):
    dicio = {}
    n = 1
    for palavra in frases:
        dicio.key(palavra) = n
        n+=1
    return dicio