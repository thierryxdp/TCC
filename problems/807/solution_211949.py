def conta_frases(texto):
    '''funcao que dado um texto retorna o numero de
    frses; str -> int'''
    a = str.count(texto,'.')
    b = str.count(texto,'!')
    c = str.count(texto,'?')
    d = str.count(texto,'...')
    
    if a>0 and d>0:
        return (a-3*d) + b + c + d
    else:
        return a + b + c + d