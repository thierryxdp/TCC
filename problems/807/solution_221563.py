def conta_frases(a):
    '''dada uma string, é informado quantas frases tem nela
       str -> int'''

    a=str.replace(a,'...','.')
    b=str.count(a,'.')
    c=str.count(a,'!')
    d=str.count(a,'?')
    
    return b+c+d