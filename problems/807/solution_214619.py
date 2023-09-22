def conta_frases(frases):
    """Retorna quandas frases existem no texto dado.
    Apenas frases terminadas com ponto final,
    ponto de exclamação e ponto de interrogação."""
    string_pontuada = frases.replace('!','.')
    string_pontuada = string_pontuada.replace('?','.')
    string_pontuada = string_pontuada.replace('...','.')
    return string_pontuada.count('.')