def conta_frases (texto):
    """Função que calcula o número de frases que um texto possui, separadas por '.', '...', '?', '!'
    entrada: string
    saída: int"""
    
    return str.count(texto, '.') and str.count(texto, '...') and str.count(texto, '?') and str.count(texto, '!')