def freq_palavras(frases):
    x = 0
    y = {}
    while x < len(str.split(frases)):
        y[str.split(frases)[x]] = str.count(str(str.split(frases)) ,str(str.split(frases)[x]))
        x = x+1 
    return y