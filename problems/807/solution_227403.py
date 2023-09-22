def conta_frases(texto):
    '''função que conta o numero de frases que aparece no texto;
    str->list'''
    ponto =  '.' and '!' and '?' and '...' 
    return len(str.split(texto,ponto))