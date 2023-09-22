def conta_frases(texto):
    '''Calcula a quantidade de frases tem em um texto; string->int'''
    return len(texto.split('.')+texto.split('?')+texto.split('!')+texto.split('...'))