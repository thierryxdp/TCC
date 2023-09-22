def freq_palavras(frase):
    d = {}
    t = str.split(frase)
    for i in t:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    return d