def conta_frases(texto):
    '''Retorna o numero de frases dentro de um texto
    str -> int'''
    return len(texto.split('!', '.', '?'))