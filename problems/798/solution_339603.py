def freq_palavras(frase):
    pal_freq = [frase.count(indice) for indice in frase]
    return dict(list(zip(frase,pal_freq)))