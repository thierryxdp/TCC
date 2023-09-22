def conta_frases(texto):
    '''conta o número de frases em um texto'''
    frases=list(texto.split('.'|'!'|'?',texto))
    return len(frases)