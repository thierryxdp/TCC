def conta_frases(texto):
    '''função que conta o numero de frases que aparece no texto;
    str->list'''
    ponto =  '.' or '!' or '?' or '...' 
    return len(str.split(texto,ponto))