def conta_frases(texto):
    '''Esta função calcula a quantidade de frases em um texto.
    str->int'''
    ponto = str.count(texto,'.')
    exclamacao = str.count(texto,'!')
    interrogacao = str.count(texto,'?')
    reticencias = str.count(texto,'...')
    if '...' in texto:
        return ponto+exclamacao+interrogacao-2*reticencias
    else:
        return ponto+exclamacao+interrogacao