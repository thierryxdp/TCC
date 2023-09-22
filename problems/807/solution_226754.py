def conta_frases(texto):
    '''conta o número de frases em um texto'''
    frases=list(texto.split('.')) or list(texto.split('!')) or list(texto.split('?'))
    return len(frases)