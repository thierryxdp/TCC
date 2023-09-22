def freq_palavras(frases):
    freq = {}
    quantidade = frases.count(palavra)
    for palavra in frases:
        freq = freq + [palavra:quantidade]
    return freq