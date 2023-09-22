def conta_frases(a):
    '''dada uma string, é informado quantas frases tem nela
       str -> int'''
    str.replace(a,'...','.')
    str.replace(a,'!','.')
    str.replace(a,'?','.')
    
    c=str.count(a,'.')
    
    return c