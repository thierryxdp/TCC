def conta_frases(texto):
    '''função que conta o numero de frases que aparece no texto;
    str->list'''
    ponto =  '.' and '!' and '?' and '...' 
    return (str.split(texto,ponto))