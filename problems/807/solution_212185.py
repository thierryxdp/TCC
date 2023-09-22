def conta_frases(texto):
    '''função que receba um texto e retorne quantas frases têm nele
    str->int'''
    
    return str.replace(texto, '...', 'abcde')
    return str.replace(texto, '.', 'abcde')
    return str.replace(texto, '!', 'abcde')
    return str.replace(texto, '?', 'abcde')
    
    return texto.count('abcde')