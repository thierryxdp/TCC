def conta_frases(texto: str) -> int:
    '''
    Retorna o número de frases dado um texto
    '''
    a1 = texto.count(.)
    a2 = texto.count(?)
    a3 = texto.count(!)
    a4 = texto.count(...)
    return a1 + a2 + a3 + a4