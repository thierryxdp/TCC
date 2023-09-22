def freq_palavras(frases):
    y = reduce( lambda d, c: d.update([(c, d.get(c,0)+1)]) or d, frases.split(), {})
    return y