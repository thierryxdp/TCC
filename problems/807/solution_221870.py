def conta_frases(texto):
    '''Função que conta as frases de um texto separadas por ".", "...", "?" ou "!"
    str -> int'''
    exclamacao = str.count(texto, '!')
    interrogacao = str.count(texto, '?')
    pontos = str.count(texto, '.')
    retcencias = str.count(texto, '...')
    num_frases = exclamacao + interrogacao + retcencias + (pontos - 3 * retcencias)
    return num_frases