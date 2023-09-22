def conta_frases(txt):
    ''' Retorna a quantidade de frases de um texto
    str -> int '''
    return txt.count('.') +  txt.count('!') + txt.count('?') +  txt.count('...')