def conta_frases(text):
    ''' Função que conta número de frases que aparecem em um texto
str->int'''
    lista=[]
    lista[:]=text
    a=list.count(lista,'.')
    b=list.count(lista,'!')
    c=list.count(lista,'?')
    d=str.count(text,'..')
    return a+b+c-(2*d)