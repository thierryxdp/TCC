def conta_frases(frases):
    """funçao que dado um texto em formato de string, conta a quantidade de frases contidas neste,
    sendo cada frase determinada por um pontofinal, ponto de exclamação, ponto de interrogação ou redicencias;
    str-->int"""
    x = str.count(frases,'...')
    y = str.count(frases, '.')
    z = str.count(frases, '?')
    w = str.count(frases, '!')
    return (y + z + w) - 2*x