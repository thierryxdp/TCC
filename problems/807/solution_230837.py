def conta_frases(texto):
    '''Essa função retorna o numero de frases de um texto'''
    a=('.'=0)
    b=('!'=0)
    c=('?'=0)
    d=('...'=0)
    frases=str.count(texto,a)+str.count(texto,b)+str.count(texto,c)+str.count(texto,d)
    return frases