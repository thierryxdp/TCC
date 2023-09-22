def conta_frases(texto):
    '''Dado um texto armazenado em uma str, faça a função conta_frases'''
    texto = str.split(texto)
    '.,!,?,...'.join(texto)
    return len(texto)