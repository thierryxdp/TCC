def conta_frases(texto):
    '''Função que conta a quantidade de frases de um texto.
    str -> int'''
    final=str.count(texto,'.')
    exclamacao=str.count(texto,'!')
    interrogacao=str.count(texto,'?')
    reticencias=str.count(texto,'...')
    return final+exclamacao+interrogacao+reticencias