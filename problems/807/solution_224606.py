def conta_frases(texto):
    '''
    	Função que recebe um texto com pontuações e retorna
        a quantidades de frases que há nele;
        str -> int
    '''
    x = str.index(texto,'.')
    y = str.count(texto,'...')
    z = str.count(texto,'!')
    a = str.count(texto,'?')
    b = x+1 - x
    c = x+2 - x
    return y+z+a+b+c