def lingua_p(palavra):
    ''' função que retorna a mesma palavra do parâmetro traduzida para a língua do P
    str -> str
    '''
    traduzida_p = []
    i = 0
    for letra in list(palavra):
        if letra in 'aeiouáéíóú'
           traduzida_p.append( letra + 'p' + letra)
        else:
            traduzida_p.append(letra)
    return ''.join(traduzida_p)