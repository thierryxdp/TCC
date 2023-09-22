def freq_palavras(frases):
    res = {key: frases.count(key) for key in frases.split()}
    return res