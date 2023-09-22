def conta_frases(texto):
    '''função que receba um texto e retorne quantas frases têm nele
    str->int'''
    
    str.replace(texto, '...','abcde')
    str.replace(texto, '.','abcde')
    str.replace(texto, '!','abcde')
    str.replace(texto, '?','abcde')
    
    return str.count(texto,'abcde')