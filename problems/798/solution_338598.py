def freq_palavras(frases):
    dicionario = {}
    for x in frases:
        dicionario[x] = str(str.count(x))
    return dicionario