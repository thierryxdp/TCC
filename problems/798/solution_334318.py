def freq_palavras(frases):
    frases=frases.split()
    dicio={}
    for palavra in frases:
        dicio[palavra]=list.count(frases,palavra)
    return dicio