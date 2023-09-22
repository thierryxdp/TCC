def conta_frases(frases):
    '''Função que conte o número de frases que aparecem nesse texto
    str->int
    '''
    w=frases.split('.')
    x=str(w).split('!')
    y=str(x).split('?')
    z=str(y).split('...')
    return len(z)-1