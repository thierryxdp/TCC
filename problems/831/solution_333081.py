def lingua_p (palavra):
    '''Traduz uma palavra para a lingua do P, str->str'''
    for elemento in palavra:
        if elemento in ('a','e','i','o','u'):
            palavra = palavra.replace (elemento, elemento + 'p' + elemento)
    return palavra