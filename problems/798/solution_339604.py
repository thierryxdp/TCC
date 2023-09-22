def freq_palavras(frase):
    pal_freq = [frase.count(indice) for indice in frase]
    return dict(list(frase,pal_freq))