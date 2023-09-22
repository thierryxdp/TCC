def conta_frases(frases):
    '''retorna em int a quantidade de frases em uma str
    str->int'''
    num = 0
    a = frases
    if '...' in frases: 
        a = str.replace(frases,'...','.')
    num = str.count(a,'.')+str.count(a,'!')+str.count(a,'?')
    return num