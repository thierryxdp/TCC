def conta_frases(texto): 
    """calcula e retorna o numero de frases em um texto"""
    return str.count(texto,"." or "..." or "!" or "?")