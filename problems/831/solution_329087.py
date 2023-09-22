def lingua_p(palavra):
    '''função que recebe palavra em português e
    retorna palavra traduzida em língua do p.
    str--> str'''
    
    traduzido_p = []
    contador = 0

    for letra in list(palavra):
        if letra in 'aeiou':
            traduzido_p.append(letra + 'p')
        else:
            traduzido_p.append(letra)

    return ''.join(traduzido_p)