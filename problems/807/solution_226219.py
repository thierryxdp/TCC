def conta_frases(texto: str) -> int:
    '''
    Retorna o número de frases dado um texto
    '''
    return texto.count(".", "!", "?", "...")