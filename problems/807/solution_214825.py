def conta_frases(texto):
    '''Função que, dado um texto em formato de string, retorna o número de frases que o texto contém; str -> int.'''
    x = str.count(texto, ".")
    y = str.count(texto, "!")
    z = str.count(texto, "?")
    w = str.count(texto, "...")
    return x + y + z + w - (3 * (str.count(texto, "..."))