def conta_frases (t):
    '''função que dado um texto (t) retorna o número de frases do texto;
    str -> int'''
    return (str.count(t,'.') - 3*str.count(t, '...')) + str.count(t,'?') + str.count(t, '!') + str.count(t, '...')