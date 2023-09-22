def conta_frases(a):
    '''dada uma string, é informado quantas frases tem nela
       str -> int'''
    b=str.count(a,'...')
    c=str.count(a,'.')
    d=str.count(a,'!')
    e=str.count(a,'?')
    
    return c+b+d+e