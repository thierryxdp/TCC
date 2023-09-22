def freq_palavras(frases):
    dic = {}
    for palavra in frases:
        quant = str.count(frases,palavra)
        dic =+ dict(palavra,quant)
    return dic