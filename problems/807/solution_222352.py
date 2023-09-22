def conta_frases(s):
    '''
    A função retorna o número de frases de um texto
    (entrada = str, saída = int)
    '''
    return len(str.split(s, '.', '?', '!'))