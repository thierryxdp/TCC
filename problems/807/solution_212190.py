def conta_frases(texto):
    '''função que receba um texto e retorne quantas frases têm nele
    str->int'''
    
    texto = str.replace(texto, '...','abcde')
    texto = str.replace(texto, '.','abcde')
    texto = str.replace(texto, '!','abcde')
    texto =str.replace(texto, '?','abcde')
    texto= str.count(texto,'abcde') 
    return texto