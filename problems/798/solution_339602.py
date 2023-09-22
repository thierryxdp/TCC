def freq_palavras(frase):
    pal_freq = [frase.count(p) for p in frase]
    return dict(list(zip(frase,pal_freq)))