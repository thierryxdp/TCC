def conta_frases(paragrafo):
    t = (str.count(paragrafo, '!')) + (str.count(paragrafo, '.')) + (str.count(paragrafo, '?')) + (str.count(paragrafo, '...'))
    if (str.count(paragrafo, '...')):
        return ((t) - 3)
    else:
        return (t)