def freq_palavras(frases):
    freq = []
    frases = frases.split()
    quant = frases.count(palavra)
    for palavra in frases:
        freq = freq + [palavra:2]
    return freq