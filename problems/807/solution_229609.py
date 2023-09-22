def conta_frases (texto):
    '''
        Dado um texto a string retorna quantas frases o texto
        possui
        str -> int
    '''
    return str.count(texto, '.' and '!' and '?' and '...')