def conta_frases(texto):
    '''Essa função retorna o numero de frases de um texto'''
    a=('.')
    b=('!')
    c=('?')
    d=('...')
    frases=(str.count(texto,a)/str.count(texto,a))+str.count(texto,b)+str.count(texto,c)+str.count(texto,d)
    return frases