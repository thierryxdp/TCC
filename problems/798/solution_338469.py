def freq_palavras(frases):
    d = {}
    for palavra in frases:
        if palavra in d:
            d[palavra] += 1
        else:
            d[palavra] = 1

def separador(frases):
    return frases.split()