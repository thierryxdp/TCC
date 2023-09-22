def freq_palavras(frases):
    res = {key: frases.count(x) for x in frases.split()}
    return res