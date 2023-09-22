def conta_frases(texto):
    '''Dado um texto, retorna a quantidade de frases dentro do texto.
    str -> int '''
    if '...' in texto:
        texto = str.replace(texto, '...', '.')
    cont = texto.count('.') + texto.count('!') + \
        texto.count('?') + texto.count('...')
    return cont