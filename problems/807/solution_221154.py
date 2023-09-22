def conta_frases(texto):
    '''
    '''
    texto=texto.split('?','!','.','...')
    return len(texto)