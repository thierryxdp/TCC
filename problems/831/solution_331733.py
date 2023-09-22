def lingua_p(palavra):
    ''' Esta função recebe uma palavra em portuquês e retorna palavra traduzida em língua do P.
    str --> str'''
    traduzindo_p = []
    cnt = 0

    for letra in list(palavra):
        if letra in 'aeiouáéíóú':
            traduzindo_p.append(letra + 'p' + letra)
        else:
            traduzindo_p.append(letra)
    return ''.join(traduzindo_p)