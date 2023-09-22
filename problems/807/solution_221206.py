def conta_frases(texto):
    '''
    '''
    texto=texto.replace('?')
    texto=texto.replace('!')
    texto=texto.replace('.')
    texto=texto.replace('...')
    return len(texto.split())