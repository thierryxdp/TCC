def conta_frases(texto):
    '''Função que, dado um texto, conta a quantidade de frases.
    str --> int'''
    return len(str.split(texto,('.'and not '...')or'!'or'?'or'...'))