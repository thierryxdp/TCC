def conta_frases(texto):
    '''
    '''
    texto=texto.split('?')
    texto=texto.split('!')
    texto=texto.split('.')
    texto=texto.split('...')
    return len(texto)