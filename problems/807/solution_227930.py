def conta_frases(texto):
    '''
    dado um texto armazenado em uma str como entrada,
    retorna a quantidade de frases contidas no texto
    dados de entrada: str
    retorna: int
    '''
    frases = str.replace(texto, '!', '.')
    frases = str.replace(frases, '?', '.')
    frases = str.replace(frases, '...', '.')
    frases = str.split(frases,'.')
    return len(frases) - 1