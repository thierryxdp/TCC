def freq_palavras(frases):
    frequencia = {}
    for palavra in frases:
        if palavra not in frases:
            frequencia[palavra] = 1
        if palavra in frases:
            frequencia[palavra] + 1
    return frequencia