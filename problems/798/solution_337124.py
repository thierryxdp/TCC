def freq_palavras(frases):
    dicio = {key: frases.count(key) for key in frases.split()}
    return dicio