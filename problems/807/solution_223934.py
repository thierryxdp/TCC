def conta_frases(frases):
    '''Função que conte o número de frases que aparecem nesse texto
    str->int
    '''
    w=frases.count('...')
    x=frases.count('?')
    y=frases.count('!')
    z=frases.count('.')
    return w+x+y+(z-(3*w))