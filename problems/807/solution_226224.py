def conta_frases(texto: str) -> int:
    '''
    Retorna o número de frases dado um texto
    '''
    a1 = texto.count(".")
    a2 = texto.count("?")
    a3 = texto.count("!")
    a4 = texto.count("...")
    a5 = a1 - (a4 * 2)
    return a2 + a3 + a5