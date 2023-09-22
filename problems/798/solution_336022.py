def freq_palavras(frases):
    x = 0
    y = 0
    for palavra in frases:
        y = str.split(frases)[x]
        x = x+1
    return y