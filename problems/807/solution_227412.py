def conta_frases(texto):
    '''função que conta o numero de frases que aparece no texto;
    str->list'''
    ponto1 =  '.' 
    ponto2 = '!'
    ponto3 = '?'
    ponto4 = '...'
    return (str.split(texto,ponto1)+str.split(texto,ponto2)+str.split(texto,ponto3)+str.split(texto,ponto4))