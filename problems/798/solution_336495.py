def freq_palavras(frases):
    frequencia = {x: frases.count(x) for x in frases.split()}
    return frequencia