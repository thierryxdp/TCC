def lingua_p(palavra):
    '''função que muda as palavras para a lingua do p; str -> str'''
    p = ('')
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            p = p + letra + 'p' + letra
        else:
            p = p + letra
    return p