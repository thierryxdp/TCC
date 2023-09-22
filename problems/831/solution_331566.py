def lingua_p(palavra):
    '''Função que recebe uma palavra em português e retorna
    esta traduzida para a lingua do P.
    str -> str
    '''
    traduz_linguaP = []

    for letra in list(palavra):
        if letra in 'aeiouáéíóú':
            traduz_linguaP.append(letra + 'p' + letra)
        else:
            traduz_linguaP.append(letra)

    return ''.join(traduz_linguaP)