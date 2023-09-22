def freq_palavras(frases):
    dicionario = {}
    for x in frases:
        if x in frases:
            dicionario[x] = str(str.count(x))
    return dicionario