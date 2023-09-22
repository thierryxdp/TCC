def conta_frases (texto):
    """Função que, dado um texto, conta o número de frases separadas por '.', '...', '?' ou '!'
    entrada: str
    saída: int"""
    str.replace('? ', '. ') and str.replace('! ', '. ') and str.replace('... ', '. ')