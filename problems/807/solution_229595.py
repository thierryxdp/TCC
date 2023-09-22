def conta_frases(texto):
    ''' recebe um texto e diz quantas frases há sendo que cada frase
    é determinado pelo termino de !,.,...,?'''
    a= str.count(texto,'.')
    b= str.count(texto,'!')
    c= str.count(texto,'?')
    d= str.count(texto,'...')
    return a+b+c+d+(d*(-3))