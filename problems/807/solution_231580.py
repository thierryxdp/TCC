def conta_frases (texto):
    '''Função que conta quantas frases há no testo.
    str->str'''
    interrogacao = str.count(texto, '?')
    exclamacao = str.count(texto, '!')
    ponto =  str.count(texto, '.')
    reticencias =  str.count(texto, '...')
    return ponto - reticencias*3 + exclamacao + interrogacao + reticencias