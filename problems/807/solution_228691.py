def conta_frases(texto):
    ''' função que armazena um texto e retorna o número de frases contidas nele.
    str -> int
    '''
    frase1 = str.split(texto, '.')
    frase2 = str.split(texto, '!')
    frase3 = str.split(texto, '?')
    frase4 = str.count(texto, '...')
    return (len(frase1) - 2*frase4) + len(frase2) + len(frase3) - 3