def conta_frases(texto):
    '''
    	Função que recebe um texto com pontuações e retorna
        a quantidades de frases que há nele;
        str -> int
    '''
    x1 = str.strip(texto,'...')
    x2 = str.count(x1,'.')
    y = str.count(texto,'...')
    z = str.count(texto,'!')
    a = str.count(texto,'?')
    return y+z+a+x