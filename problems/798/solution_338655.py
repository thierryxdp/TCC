def freq_palavras(x):
    y = dict()
    for frase in frases.split():
        if frase in resultado:
            y[x] += 1
        else:
            y[x] = 1
    return y