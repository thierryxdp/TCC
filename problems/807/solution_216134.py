def conta_frases(texto):
    '''Função que dado um texto como parâmetro de entrada, 
    retona a quantidade de frases que ele possui.
    str->int'''
    return str.count(texto,'.')+str.count(texto,'!')+str.count(texto,'?')-2*str.count(texto,'...')