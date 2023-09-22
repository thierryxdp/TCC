def conta_frases(texto):
    '''Dado um texto, retorna a quantidade de frases dentro do texto.
    str -> int '''
    cont = texto.count('.') + texto.count('!') + \
        texto.count('?') + texto.count('...') - 1
    return cont