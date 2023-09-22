def freq_palavras(frases):
    d = dict()
    frases1 = str.split(frases,' ')
    for i in frases1:         
        if i not in d:
            d[i] = 0
        if i in d:
            d[i] += 1
    return d