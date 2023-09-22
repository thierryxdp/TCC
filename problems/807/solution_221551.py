def conta_frases(a):
    '''dada uma string, é informado quantas frases tem nela
       str -> int'''
    str.replace(a,'...','.')
    c=str.count(a,'.')
    d=str.count(a,'!')
    e=str.count(a,'?')
    
    return c+d+e