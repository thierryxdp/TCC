def uppCons(x):
    '''Esta função recebe uma string e torna maiúscula as consoantes
    assinatura str -> str'''
    a = ''
    for c in x:
        if c in 'bcdfghjklmnpqrstvxwyzç':
            a +=str.upper(c)
        else:
            a += c
    return a