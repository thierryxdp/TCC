def lingua_p(palavra): e 
    '''Função que recebe palavra em português e retorna 
    palavra traduzida em língua do p. str --> str'''
    p_traduz = []
    i = 0
    for letra in list(palavra):
        if letra in 'aeiouáéíóú':
            p_traduz.append(letra + 'p' + letra)
        else:
             p_traduz.append(letra)
    return ''.join(p_traduz)