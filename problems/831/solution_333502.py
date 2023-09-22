def lingua_p(palavra):
    '''A função recebe uma palavra em
    português e traduz para a língua do p
    str --> str'''
    
    traduzp = []
    counter = 0
    
    for letra in list(palavra):
        if letra in 'aeiouáéíóú':
            traduzp.append(letra + 'p' + letra)
        else:
            traduzp.append(letra)
     
    return ''.join(traduzp)