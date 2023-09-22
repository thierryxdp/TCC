def conta_frases(frases):
    """Retorna quandas frases existem no texto dado.
    Apenas frases terminadas com ponto final,
    ponto de exclamação e ponto de interrogação."""
    s = frases
    if '.' in s:
        return len(str.split(s))