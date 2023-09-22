def conta_frases(texto):
    '''Retorna o número de frases de um texto
    string -> int '''
    return texto.count('.')+texto.count('?')+texto.count('!')