def conta_frases(texto):
    '''Função que conta o número de frases que aparecem em um texto dado.
    str-->int'''
    reticencias = texto.count('...')
    final = texto.count('.')
    exclamacao = texto.count('!')
    interrogacao = texto.count('?')
    return (final-(3*reticencias) + exclamacao + reticencias + interrogacao)