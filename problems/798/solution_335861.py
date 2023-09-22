def freq_palavras(frases):
    freq = {}
    frases = frases.split()
    for palavra in frases:
        freq = freq + [palavra]=1
    return freq