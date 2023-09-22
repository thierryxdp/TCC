def lingua_p (palavra):
    '''Traduz uma palavra para a lingua do P, str->str'''
    for elemento in range(palavra):
        if elemento in ('a','á','â','ã','e','é','ê','i','í','î','o','ó','ô','õ','u','ú','û'):
            palavra.replace (elemento, elemento + 'p' + elemento)
    return palavra