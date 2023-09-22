def conta_frases(texto):
    a=('.')
    b=('!')
    c=('?')
    d=('...')
    frases=str.count(texto,a)+str.count(texto,b)+str.count(texto,c)+str.count(texto,d)-3*str.count(texto,d)
    return frases