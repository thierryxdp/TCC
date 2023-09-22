def conta_frases(texto):
    """Função que retorna o número de frases contidas em um texto;
    string -> int"""
    quantidadet = len(texto.split('.' or '!' or '?' or '...'))
    
    return quantidadet