def uppCons(f):
    '''Dada uma frase, retorna com todas consoantes em maiúsculas.
assinatura: string --> string'''
    s = ''
    for c in f:
        if c in 'bcdfghjklmnpqrstvxwyzç':
            s += c.upper() 
        else: 
            s += c
    return s