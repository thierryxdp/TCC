def conta_frases(texto):
    '''Função que conta o número de frases que aparecem em um texto dado.
    str-->int'''
    retic = texto.count('...')
    final = texto.count('.')
    exclamacao = texto.count('!')
    inter = texto.count('?')
    return (final-(3*retic) , exclamacao , retic , inter)