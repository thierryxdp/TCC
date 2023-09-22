def conta_frases(texto):
    ''' Essa função conta o número de frases de um texto
    determinado, onde cada frase termina com um ponto
    final, um ponto de exclamação, um ponto de interrogação
    ou reticências, str->int. '''
    p_final = texto.count('.')
    p_exc = texto.count('!')
    p_int = texto.count('?')
    p_ret = texto.count('...')
    return p_final+p_exc+p_int+p_ret