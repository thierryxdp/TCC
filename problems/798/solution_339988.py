def freq_palavras(frase):
    freq_palavras = [frase.count(p) for p in frase]
    return dict(list(zip(freq_palavras)))