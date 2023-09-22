def freq_palavras(frases):
    d = {}
    for palavras in frases:
        if palavras in d:
            d[palavras] += 1
        else:
            d[palavras] = 1
    return d