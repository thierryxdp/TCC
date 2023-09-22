def freq_palavras(frases):
    freq = {}
    for i in range(len(frases)):
        freq = {frases[i]: str.count(frases[i])}
    return freq