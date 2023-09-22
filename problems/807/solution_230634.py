def conta_frases(paragrafo):
    e = (str.count(paragrafo, '...'))
    t = (str.count(paragrafo, '!')) + (str.count(paragrafo, '.')) + (str.count(paragrafo, '?')) + (str.count(paragrafo, '...'))
    if (str.count(paragrafo, '...')):
        return ((t) - 3*e)
    else:
        return (t)