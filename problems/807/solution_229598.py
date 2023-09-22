def conta_frases (texto):
    '''
        Dado um texto a string retorna quantas frases o texto
        possui
        str -> int
    '''
    return len(str.split('.' or '!' or '?' or '...'))