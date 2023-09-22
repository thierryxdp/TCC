def freq_palavras(frases):
    d = {}
 
    palavras = frases.split()
    for palavra in palavras:
        if palavra not in d:
            d[palavra] = 1
        else:
            d[palavra] += 1
    return d