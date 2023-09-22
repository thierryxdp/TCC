def freq_palavras(frases):
    dicio = { key: frase.count(key) for key in frase.split()}