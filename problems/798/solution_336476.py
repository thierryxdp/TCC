def freq_palavras(frases):
    res = {x: frases.count(x) for x in frases.split()}
    return res