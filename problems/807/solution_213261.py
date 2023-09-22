def conta_frases (texto):
    """Função que calcula o número de frases que um texto possui, separadas por '.', '...', '?', '!'
    entrada: string
    saída: int"""
    
    return str.replace(texto,'...','.') and str.replace(texto,'?','.') and str.replace(texto,'!','.') and len(str.split(texto,'.')