def freq_palavras(frases):
    dicionario = {}
    for x in frases:
        dicionario[x] = str(str.count(frases,x))
    return dicionario