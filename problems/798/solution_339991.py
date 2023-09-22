def freq_palavras(frase):
    freq = [frase.count(p) for p in frase]
    return dict(list(zip(frase,freq_palavras)))