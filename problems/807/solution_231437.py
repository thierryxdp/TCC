def conta_frases(frases):
    """conta o número de frases que aparecem no texto
    str->int"""
    return frases.count(".")-(3*frases.count("...")) + frases.count("!")+frases.count("?")+frases.count("...")