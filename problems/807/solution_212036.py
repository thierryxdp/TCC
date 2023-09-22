def conta_frases(texto):
    '''Função que, dado um texto, conta a quantidade de frases.
    str --> int'''
    exclamacoes = str.count(texto,'!')
    pontos = str.count(texto,'.')
    interrogacoes = str.count(texto,'?')
    reticencias = str.count(texto,'...')
    frases = exclamacoes + pontos + interrogacoes + reticencias - 3*reticencias
    return frases