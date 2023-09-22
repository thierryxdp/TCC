def conta_frases(texto):
    '''funcao que conta o numero de frases de um dado texto
    str-> int'''
    texto= str.replace(texto,'...', '#')
    return str.count(texto, '?')+str.count(texto, '!')+ str.count(texto,'#')+str.count(texto, '.')