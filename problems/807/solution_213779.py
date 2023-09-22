def conta_frases(texto):
    """ """
    
    fim = '.' or '!' or '?' or '...'
    
    return str.split(texto,fim)