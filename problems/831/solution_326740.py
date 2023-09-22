def lingua_p(palavra):
    '''Essa função irá traduzir uma palavra em portugues para a lingua do P.
    entrada -> str
    saida -> str'''
    
    palavra = list(str.lower(palavra))
    
    for i in range(len(palavra)):
        if palavra[i] in 'aáâeéêiíoóôuú':
            palavra[i] = palavra[i] + 'p' + palavra[i]

    palavra = str.join('', palavra)
    
    return palavra