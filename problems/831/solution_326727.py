def lingua_p(palavra):
    '''Funcao que traduz uma palavra em portugues para a lingua do P.
    str -> str'''
    
    palavra = list(str.lower(palavra))
    
    for i in range(len(palavra)):
        if palavra[i] in 'aeiou':
            palavra[i] = palavra[i] + 'p' + palavra[i]

    palavra = str.join('', palavra)
    
    return palavra