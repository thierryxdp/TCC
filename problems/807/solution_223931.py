def conta_frases(frases):
    '''Função que conte o número de frases que aparecem nesse texto
    str->int
    '''
    w=frases.split('...'or'?'or'!'or'.')
    
    return len(w)