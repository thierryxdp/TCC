def conta_frases(x):
    '''função que dado uma string, retorna a quantidade de frases que terminam com ponto
    de exclamação, ponto de interrogação, três pontos ou reticências
    str -> int'''
    x = str.replace(x,'...','!')
    return str.count(x,'.')+ str.count(x,'!')+ str.count(x,'?')