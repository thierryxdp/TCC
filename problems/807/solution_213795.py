def conta_frases(texto):
    """ """
    
    fim = '.' or '!' or '?' or '...'
    
    return len(str.split(texto,'!' or '.' or '...'))