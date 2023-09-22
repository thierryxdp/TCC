def freq_palavras(frases):
    a = frases.split()
    d = {}
    for i in a:
        if i in d:
            d[i] = d[i]+1
        else:
            d[i] = 1