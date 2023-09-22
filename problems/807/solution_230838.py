def conta_frases(texto):
    '''Essa função retorna o numero de frases de um texto'''
    a=('.')
    b=('!')
    c=('?')
    d=('...')
    frases=str.count(texto,a=0)+str.count(texto,b=0)+str.count(texto,c=0)+str.count(texto,d=0)
    return frases