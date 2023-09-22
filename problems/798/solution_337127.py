def freq_palavras(frases):
    dicio = {key: frases.count(frases.split(key)) for key in frases.split()}
    return dicio