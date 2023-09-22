def conta_frases (texto):
    """Função que, dado um texto, retorna seu número de frases
    entrada: string
    saída: int"""
    return str.count(texto,'.')+str.count(texto,'!')+str.count(texto,'?')+str.count(texto,'...')