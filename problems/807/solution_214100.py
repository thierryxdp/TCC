def conta_frases(texto):
    '''Função que, dado um texto no formato de string, retorna o número de frases do texto; str -> int.'''
    frases = str.split(texto)
    return len(frases)