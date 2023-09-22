def conta_frases(texto):
    '''funcao que conta o numero de frases de um dado texto;
    str-> int'''
    return str.count(texto,'?')+str.count(texto, '!')+str.count(texto[0:-1], '. ')+str.count(texto[0:-1],'... ')+1