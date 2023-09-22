def conta_frases(texto):
    '''Função que calcula o número de frases de um texto
    str -> int'''
    frases = str.split(texto, '.', '!', '?', '...')
    numero_frases = len(frases)
    return numero_frases