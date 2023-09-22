def conta_frases (texto):
    """Função que conta o número de frases contidas em um texto, separadas por pontos finais
    entrada: string
    saída: int"""
    return len(str.split(texto, '.')) + len(str.split(texto, '...')) + len(str.split(texto, '?')) + len(str.split(texto, '!'))