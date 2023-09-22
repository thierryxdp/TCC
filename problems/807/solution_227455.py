def conta_frases(texto):
    ''' conta o número de frases em um texto dado de entrada str->int '''
    return texto.count('.')+texto.count('!')+texto.count('?')+texto.count('...')