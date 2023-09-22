def freq_palavras(frases):
    """ função recebe frases, corta elas com split e depois conta as palavras"""
    y = reduce( lambda d, c: d.update([(c, d.get(c,0)+1)]) or d, frases.split(), {})
    return y