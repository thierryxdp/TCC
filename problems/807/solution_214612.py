def conta_frases(frases):
    """Retorna quandas frases existem no texto dado.
    Apenas frases terminadas com ponto final,
    ponto de exclamação e ponto de interrogação."""
    
    return str.replace(frases,'.' or '!' or '?' or '...')