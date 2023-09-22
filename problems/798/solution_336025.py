def freq_palavras(frases):
    x = 0
    y = 0
    while x < len(str.split(frases)):
        y = str.split(frases)[0]
        x = x+1
    return len(y)