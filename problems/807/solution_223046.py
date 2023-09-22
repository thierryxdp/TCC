def conta_frases(texto):
    '''funcao que conta o numero de frases de um dado texto;
    str-> int'''
    texto=str.replace(texto, '?', ',' )
    texto=str.replace(texto, '!', ',' )
    texto=str.replace(texto, '.', ',' )
    texto=str.replace(texto, '...', ',' )
    return len(texto)