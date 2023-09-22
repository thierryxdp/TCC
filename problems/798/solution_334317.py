def freq_palavras(frases):
    dicio={}
    for palavra in frases:
        dicio[palavra]=list.count(frases,palavra)
    return dicio