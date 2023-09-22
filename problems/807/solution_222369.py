def conta_frases(s):
    '''
    A função retorna o número de frases de um texto
    (entrada = str, saída = int)
    '''
    d = str.replace(s, '...', '[]')
    return str.count(d, '.') + str.count(d, '[]') + str.count(d, '?') + str.count(d, '!')