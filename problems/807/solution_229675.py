def conta_frases(x):
    'Função que retorna a quantidade de frases em um texto.'
    'str->int'
    a=str.count(x,'!')+str.count(x,'?')
    b=str.count(x,'...')
    c=str.count(x,'.')
    d=c-(3*b)
    return a+b+d